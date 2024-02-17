# -*- coding: utf-8 -*-
from __future__ import unicode_literals  # string literals are all unicode
from __future__ import division  # if python 2, force truediv division (default in 3)

import base64
import logging
import unittest
import uuid
import time
import sys
import os
import functools

from . import bridge
from . import test_module

if sys.version_info[0] == 2:
    from socket import (
        error as ConnectionRefusedError,
    )  # ConnectionRefusedError not defined in python2, this is next closest thing


def print_stats(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start_stats = self.test_bridge.get_stats()
        func(self, *args, **kwargs)
        print(
            "\n{}:\n\t{}\n".format(
                func.__name__, self.test_bridge.get_stats() - start_stats
            )
        )

    return wrapper


def test_unindented_function():
    """ Test function used to remoteify to make sure we can still send unindented stuff """
    return 50


class TestBridge(unittest.TestCase):
    """ Assumes there's a bridge server running at DEFAULT_SERVER_PORT """

    @classmethod
    def setUpClass(cls):
        port = int(os.environ.get("TEST_PORT", bridge.DEFAULT_SERVER_PORT))
        cls.test_bridge = bridge.BridgeClient(
            connect_to_port=port, loglevel=logging.DEBUG, record_stats=True
        )
        cls.total_start_stats = cls.test_bridge.get_stats()

    @classmethod
    def tearDownClass(cls):
        total_stats = cls.test_bridge.get_stats()
        print(
            "\n{}:\n\t{}\n".format(
                "TestBridge Total", cls.test_bridge.get_stats() - cls.total_start_stats
            )
        )

    @print_stats
    def test_import(self):
        mod = self.test_bridge.remote_import("base64")
        self.assertTrue(mod is not None)

    @print_stats
    def test_call_no_args(self):

        mod = self.test_bridge.remote_import("uuid")

        result = mod.uuid4()

        self.assertTrue(result is not None)

    @print_stats
    def test_call_arg(self):
        # also tests call with bytestring arg in python3

        mod = self.test_bridge.remote_import("base64")

        test_str = str(uuid.uuid4())

        result_str = None
        if sys.version[0] == "3":
            result = mod.b64encode(test_str.encode("utf-8"))
            result_str = base64.b64decode(result).decode("utf-8")
        else:
            # python2 can't send a byte string, and if the other end is python3, b64encode won't work on a string.
            # instead we'll try creating a uuid from the string
            remote_uuid = self.test_bridge.remote_import("uuid")
            new_uuid = remote_uuid.UUID(test_str)
            result_str = str(new_uuid)

        self.assertEqual(test_str, result_str)

    @print_stats
    def test_call_multi_args(self):
        mod = self.test_bridge.remote_import("re")

        remote_obj = mod.compile("foo", mod.IGNORECASE)

        self.assertTrue(remote_obj is not None)

        self.assertTrue(remote_obj.match("FOO") is not None)

    @print_stats
    def test_call_with_remote_obj(self):

        mod = self.test_bridge.remote_import("uuid")

        remote_obj = mod.uuid4()
        result = str(remote_obj)
        self.assertTrue(result is not None)
        self.assertTrue("-" in result and "4" in result)

    @print_stats
    def test_call_with_str(self):
        """ also tests calling str() on remote obj """

        mod = self.test_bridge.remote_import("uuid")

        test_uuid_str = "00010203-0405-0607-0809-0a0b0c0d0e0f"

        remote_uuid = mod.UUID(test_uuid_str)
        self.assertTrue(remote_uuid is not None)
        result = str(remote_uuid)
        self.assertEqual(test_uuid_str, result)

    # bool, int, list, tuple, dict, bytes, bridge object, callback, exception, none
    # set a function into the remote __main__/globals() to call
    # callback as key func in list.sort

    @print_stats
    def test_call_kwargs(self):
        self.skipTest("Not implemented yet")

    @print_stats
    def test_get(self):
        mod = self.test_bridge.remote_import("uuid")
        remote_doc = mod.__doc__
        self.assertTrue("RFC 4122" in remote_doc)

    @print_stats
    def test_set(self):
        test_string = "hello world"
        mod = self.test_bridge.remote_import("__main__")
        mod.test = test_string

        self.assertEqual(test_string, mod.test)

    @print_stats
    def test_get_non_existent(self):
        """ Check that requesting a non-existent attribute over the bridge raises an attributeerror """
        mod = self.test_bridge.remote_import("re")

        remote_obj = mod.compile("foo")

        with self.assertRaises(AttributeError):
            remote_obj.doesnt_exist

    @print_stats
    def test_get_callable(self):
        mod = self.test_bridge.remote_import("re")

        remote_obj = mod.compile("foo")

        remote_callable = remote_obj.search
        self.assertTrue(isinstance(remote_callable, bridge.BridgedCallable))

    @print_stats
    def test_callable(self):
        mod = self.test_bridge.remote_import("re")

        remote_obj = mod.compile("foo")

        remote_callable = remote_obj.match

        self.assertTrue(remote_callable("fooa") is not None)

    @print_stats
    def test_serialize_deserialize_types(self):
        mod = self.test_bridge.remote_import("__main__")
        remote_list = mod.__builtins__.list

        # assemble a list of different types
        # Note: we include False now to detect failure to correctly unpack "False" strings into bools
        test_list = [
            1,
            0xFFFFFFFF,
            True,
            False,
            "string",
            "unicode_string🐉🔍",
            (1, 2, 3),
            [4, 5, 6],
            {7: 8, 9: 10},
            uuid.uuid4(),
            pow,
            1.5,
        ]

        # send the list in to create a remote list (which comes straight back)
        created_list = remote_list(test_list)

        # check it's the same
        self.assertEqual(test_list, created_list)

    @print_stats
    def test_serialize_deserialize_bytes(self):
        """ byte strings across 2<->3 bridges will be forced to strings (because py2 treats bytes and strs as the same thing """
        mod = self.test_bridge.remote_import("__main__")
        remote_list = mod.__builtins__.list

        test_list = [b"bytes"]

        # send the list in to create a remote list (which comes straight back)s
        created_list = remote_list(test_list)

        # check it's the same, either as a byte or normal string
        self.assertTrue(
            created_list[0] == test_list[0]
            or created_list[0] == test_list[0].decode("utf-8")
        )

    @print_stats
    def test_serialize_deserialize_bridge_object(self):
        # bridge objects TODO
        self.skipTest("Not implemented yet")

    @print_stats
    def test_none_result(self):
        mod = self.test_bridge.remote_import("re")

        remote_obj = mod.compile("foo")

        remote_callable = remote_obj.search

        self.assertTrue(remote_callable("abar") is None)

    @print_stats
    def test_exception(self):
        self.skipTest("Not implemented yet")

    @print_stats
    def test_callback(self):
        """ Test we correctly handle calling back to here from across the bridge """

        def sort_fn(val):
            return len(val)

        mod = self.test_bridge.remote_import("__main__")
        remote_sorted = mod.__builtins__.sorted

        test_list = ["aaa", "bb", "c"]
        sorted_list = remote_sorted(test_list, key=sort_fn)

        self.assertEqual(sorted(test_list, key=sort_fn), sorted_list)

    @print_stats
    def test_remote_iterable(self):
        """ Test we can access values from a remote iterable """
        mod = self.test_bridge.remote_import("__main__")
        remote_range = mod.__builtins__.range

        remote_it = remote_range(4, 10, 2)

        it_values = list(remote_it)

        self.assertEqual(list(range(4, 10, 2)), it_values)

    @print_stats
    def test_remote_iterable_for(self):
        """ Test we can access values from a remote iterable with a for loop """
        mod = self.test_bridge.remote_import("__main__")
        remote_range = mod.__builtins__.range

        remote_it = remote_range(4, 10, 2)
        it_values = list()
        for value in remote_it:
            it_values.append(value)

        self.assertEqual(list(range(4, 10, 2)), it_values)

    @print_stats
    def test_float(self):
        """ Test we can sent a float value """
        remote_time = self.test_bridge.remote_import("time")
        remote_time.sleep(0.1)

    @print_stats
    def test_is_bridged_object(self):
        remote_uuid = self.test_bridge.remote_import("uuid")

        remote_obj = remote_uuid.uuid4()
        local_obj = uuid.uuid4()

        self.assertTrue(bridge._is_bridged_object(remote_obj))
        self.assertFalse(bridge._is_bridged_object(local_obj))

    @print_stats
    def test_bridged_isinstance(self):
        mod = self.test_bridge.remote_import("__main__")
        remote_float = mod.__builtins__.float
        remote_int = mod.__builtins__.int
        remote_uuid = self.test_bridge.remote_import("uuid")
        remote_class = remote_uuid.UUID
        remote_obj = remote_uuid.uuid4()
        local_class = uuid.UUID
        local_obj = uuid.uuid4()

        # local obj, local class
        self.assertTrue(bridge.bridged_isinstance(local_obj, local_class))
        self.assertFalse(bridge.bridged_isinstance(local_obj, float))

        # local obj, fully local tuple
        self.assertTrue(bridge.bridged_isinstance(local_obj, (float, local_class)))
        self.assertFalse(bridge.bridged_isinstance(local_obj, (float, int)))

        # local obj, mixed tuple
        self.assertTrue(
            bridge.bridged_isinstance(local_obj, (remote_class, float, local_class))
        )
        self.assertFalse(
            bridge.bridged_isinstance(local_obj, (remote_float, float, int))
        )

        # local obj, remote class
        self.assertFalse(bridge.bridged_isinstance(local_obj, remote_class))

        # local obj, fully remote tuple
        self.assertFalse(
            bridge.bridged_isinstance(local_obj, (remote_float, remote_class))
        )

        # remote obj, local class
        self.assertFalse(bridge.bridged_isinstance(remote_obj, local_class))

        # remote obj, fully local tuple
        self.assertFalse(bridge.bridged_isinstance(remote_obj, (float, local_class)))

        # remote obj, mixed tuple
        self.assertTrue(
            bridge.bridged_isinstance(remote_obj, (remote_class, float, local_class))
        )
        self.assertFalse(
            bridge.bridged_isinstance(remote_obj, (remote_float, float, int))
        )

        # remote obj, remote class
        self.assertTrue(bridge.bridged_isinstance(remote_obj, remote_class))
        self.assertFalse(bridge.bridged_isinstance(remote_obj, remote_float))

        # remote obj, fully remote tuple
        self.assertTrue(
            bridge.bridged_isinstance(remote_obj, (remote_float, remote_class))
        )
        self.assertFalse(
            bridge.bridged_isinstance(remote_obj, (remote_float, remote_int))
        )

    @print_stats
    def test_bridged_get_type(self):
        """ Make sure we can get an object representing the type of a bridged object """
        remote_uuid = self.test_bridge.remote_import("uuid")
        remote_obj = remote_uuid.uuid4()

        self.assertTrue("<class 'uuid.UUID'>" in str(remote_obj._bridged_get_type()))
        self.assertTrue(
            "'type'" in str(remote_obj._bridged_get_type()._bridged_get_type())
        )

    @print_stats
    def test_remote_eval(self):
        self.assertEquals(3, self.test_bridge.remote_eval("1+2"))

    @print_stats
    def test_remote_eval_bad_code(self):
        with self.assertRaises(bridge.BridgeException):
            self.test_bridge.remote_eval("1+x")

    @print_stats
    def test_remote_eval_kwargs(self):
        self.assertEquals(3, self.test_bridge.remote_eval("x+y", x=1, y=2))

    @print_stats
    def test_remote_eval_timeout(self):
        remote_time = self.test_bridge.remote_import("time")

        # check that it times out if not enough time allocated
        with self.assertRaises(bridge.BridgeTimeoutException):
            self.test_bridge.remote_eval(
                "sleep(2)", timeout_override=1, sleep=remote_time.sleep
            )

        # check that it works with enough time
        self.test_bridge.remote_eval(
            "sleep(2)", timeout_override=3, sleep=remote_time.sleep
        )

    @print_stats
    def test_operators(self):
        # check we can handle operator comparisons, addition, etc
        remote_datetime = self.test_bridge.remote_import("datetime")
        td1 = remote_datetime.timedelta(1)
        td2 = remote_datetime.timedelta(2)

        self.assertTrue(td1 < td2)
        self.assertTrue(td2 >= td1)
        self.assertEquals(remote_datetime.timedelta(3), td1 + td2)
        self.assertEquals(td1, td2 // 2)  # we use floordiv here, truediv tested below

    @print_stats
    def test_truediv(self):
        # check we cleanly fallback from truediv to div
        # timedelta in jython2.7 implements __div__ but not __truediv__
        remote_datetime = self.test_bridge.remote_import("datetime")
        td1 = remote_datetime.timedelta(1)
        td2 = remote_datetime.timedelta(2)
        self.assertEquals(td1, td2 / 2)

    @print_stats
    def test_len(self):
        # check we can handle len
        remote_collections = self.test_bridge.remote_import("collections")
        dq = remote_collections.deque()
        dq.append(1)
        dq.append(2)
        dq.append(3)
        self.assertEquals(3, len(dq))

    @print_stats
    def test_bool(self):
        """ check we handle truthiness """
        remote_collections = self.test_bridge.remote_import("collections")
        dq = remote_collections.deque()
        self.assertFalse(bool(dq))

        dq.append(1)
        self.assertTrue(bool(dq))

        # check we handle custom truthiness
        class x:
            def __init__(self, y):
                self.y = y

            def __bool__(self):
                return self.y == 2

            __nonzero__ = __bool__

        f = x(3)
        self.assertFalse(self.test_bridge.remote_eval("bool(f)", f=f))
        t = x(2)
        self.assertTrue(self.test_bridge.remote_eval("bool(t)", t=t))

    @print_stats
    def test_bytes(self):
        """ Test that we handle calling bytes() on a bridged object """
        remote_collections = self.test_bridge.remote_import("collections")
        dq = remote_collections.deque()
        dq.append(1)

        if sys.version_info[0] == 2:
            # bytes() == str() in py 2
            self.assertEquals(bytes(dq), "deque([1])")
        else:
            self.assertEquals(bytes(dq), b"\x01")

    @print_stats
    def test_remote_inheritance(self):
        """ check that we can inherit from a remote type """
        remote_collections = self.test_bridge.remote_import("collections")
        remote_deque = remote_collections.deque

        class new_deque(remote_deque):
            def __init__(self, test):
                remote_deque.__init__(self)
                self.test = test
                self.called = False

            def append(self, x):
                remote_deque.append(self, x)
                self.called = True

        nd = new_deque("test")
        self.assertEquals(nd.test, "test")

        nd.append(1)
        self.assertTrue(nd.called)
        self.assertEquals(nd.pop(), 1)

        self.assertTrue(
            not isinstance(nd.append, bridge.BridgedCallable),
            "Expected local implementation to stay local - is actually: "
            + str(type(nd.append)),
        )

    @print_stats
    def test_nonreturn(self):
        """ Test we can call a bridged function as non-returning
        """
        remote_time = self.test_bridge.remote_import("time")
        # would expect this to timeout - but instead should send off and keep going
        remote_time.sleep._bridge_call_nonreturn(10)

    @print_stats
    def test_nonreturn_doesnt_respond(self):
        """ Test that a nonreturn call doesn't cause a response to show up
        """
        remote_collections = self.test_bridge.remote_import("collections")
        dq = remote_collections.deque()
        # let any responses in flight trickle home
        time.sleep(1)
        # record the size of the response manager
        response_count = len(self.test_bridge.client.response_mgr.response_dict)
        # expect no response
        dq.append._bridge_call_nonreturn(1)
        # let any responses in flight trickle home
        time.sleep(1)
        # check that there aren't more responses
        self.assertTrue(
            response_count >= len(self.test_bridge.client.response_mgr.response_dict)
        )

    @print_stats
    def test_nonreturn_marker_remote(self):
        """ Test that a callable marked as nonreturn doesn't return when called normally
        """
        remote_main = self.test_bridge.remote_import("__main__")
        # would normally time out
        remote_main.nonreturn()

    @print_stats
    def test_nonreturn_marker_local(self):
        """ Test that a callable marked as nonreturn doesn't return when called normally from the other side of the bridge
        """

        class Callback:
            called = False

            @bridge.nonreturn
            def callback(self):
                self.called = True
                # cause a timeout
                time.sleep(10)

        c = Callback()

        self.test_bridge.remote_eval("c.callback()", c=c, timeout_override=1)
        # pause to let the callback land
        time.sleep(1)
        self.assertTrue(c.called)

    @print_stats
    def test_remoteify_simple_function(self):
        """ Test that we can remoteify a simple function """

        def foobar():
            return True

        remote_foobar = self.test_bridge.remoteify(foobar)

        self.assertTrue(remote_foobar())

    @print_stats
    def test_remoteify_unindented(self):
        """ Test that we can remoteify a function that isn't indented"""

        remote_unindented_function = self.test_bridge.remoteify(
            test_unindented_function
        )

        self.assertEquals(50, remote_unindented_function())

    @print_stats
    def test_remoteify_same_names(self):
        """ Test that we can remoteify some functions with the same name """

        def foobar():
            return 10

        remote_foobar10 = self.test_bridge.remoteify(foobar)

        def foobar():
            return 20

        remote_foobar20 = self.test_bridge.remoteify(foobar)

        self.assertEquals(10, remote_foobar10())
        self.assertEquals(20, remote_foobar20())

    @print_stats
    def test_remoteify_function_with_args(self):
        """ Test that we can remoteify a function that takes arguments """

        def square(value):
            return value * value

        remote_square = self.test_bridge.remoteify(square)

        self.assertEquals(4, remote_square(2))

    @print_stats
    def test_remoteify_function_with_kwargs(self):
        """ Test that we can remoteify a function and supply kwargs to the definition """

        def flam():
            return defined_value

        remote_flam = self.test_bridge.remoteify(flam, defined_value=30)
        self.assertEquals(30, remote_flam())

    @print_stats
    def test_remoteify_function_with_imports(self):
        """ Test that we can remoteify a function that uses imported modules """

        def importer(val):
            from collections import deque

            d = deque()
            d.append(val)
            return d

        remote_importer = self.test_bridge.remoteify(importer)
        self.assertEquals(10, remote_importer(10).pop())

    @print_stats
    def test_remoteify_class(self):
        """ Test that we can remoteify a class """

        class CLZ:
            def __init__(self, val):
                self.val = val

        remote_clz = self.test_bridge.remoteify(CLZ)

        rc = remote_clz(20)
        self.assertEquals(20, rc.val)

    @print_stats
    def test_remoteify_class_with_inheritance(self):
        """ Test that we can remoteify a class that inherits from a remote class """
        remote_deque = (
            object  # lie to inspect locally that we're just inheriting from object
        )

        class new_deque(remote_deque):
            def __init__(self, test):
                remote_deque.__init__(self)
                self.test = test
                self.called = False

            def append(self, x):
                remote_deque.append(self, x)
                self.called = True

        remote_collections = self.test_bridge.remote_import("collections")
        remote_deque = remote_collections.deque

        remote_new_deque = self.test_bridge.remoteify(
            new_deque, remote_deque=remote_deque
        )

        nd = remote_new_deque("test")
        self.assertEquals(nd.test, "test")

        nd.append(1)
        self.assertTrue(nd.called)
        self.assertEquals(nd.pop(), 1)

        self.assertTrue(
            isinstance(nd.append, bridge.BridgedCallable),
            "Expected remoteified implementation to be remote - is actually: "
            + str(type(nd.append)),
        )

    @print_stats
    def test_remoteify_module(self):
        """ Check we can remoteify a module """
        remote_test_module = self.test_bridge.remoteify(test_module)
        remote_sys = self.test_bridge.remote_import("sys")
        self.assertEquals(remote_sys.version_info[0], remote_test_module.run())

    @print_stats
    def test_unicode_strings_only_when_required(self):
        """ Moving away from old behaviour of forcing all strings across the bridge into python 2 to be unicode
            Instead, they'll now be forced to unicode, then attempt to drop back to plain strings. """
        remote_sys = self.test_bridge.remote_import("sys")
        remote_python_version = remote_sys.version_info[0]
        local_python_version = sys.version_info[0]

        # only relevant to test when python 2 is in the mix, either local or remote
        if local_python_version == 3 and remote_python_version == 3:
            self.skipTest("Test irrelevant for non python 2 setups")

        if remote_python_version == 2:
            # send the remote side strings that are plain and unicode and check what we get
            plain_string = "string"
            unicode_string = "unicode_string🐉🔍"

            self.assertFalse(
                self.test_bridge.remote_eval(
                    "isinstance(plain_string, unicode)", plain_string=plain_string
                )
            )
            self.assertTrue(
                self.test_bridge.remote_eval(
                    "isinstance(unicode_string, unicode)", unicode_string=unicode_string
                )
            )

        if local_python_version == 2:
            # get the remote side to send us strings that are plain and unicode and check what we get
            self.assertFalse(
                isinstance(self.test_bridge.remote_eval("'plain'"), unicode)
            )
            self.assertTrue(
                isinstance(
                    self.test_bridge.remote_eval(
                        "bytearray([240, 159, 144, 137]).decode('utf-8')"
                    ),
                    unicode,
                )
            )  # dragon emoji

        else:
            # same versions, can't think of anything useful to test load
            self.skipTest("Test irrelevant for matched versions")


class TestBridgeHookImport(unittest.TestCase):
    """ Assumes there's a bridge server running at DEFAULT_SERVER_PORT."""

    @classmethod
    def setUpClass(cls):
        port = int(os.environ.get("TEST_PORT", bridge.DEFAULT_SERVER_PORT))
        cls.test_bridge = bridge.BridgeClient(
            connect_to_port=port,
            loglevel=logging.DEBUG,
            hook_import=True,
            record_stats=True,
        )

    @print_stats
    def test_hook_import_top_level(self):
        """ Test that we handle import x syntax """
        import test_hook_import_top_level

        remote_name = str(test_hook_import_top_level)
        self.assertTrue(
            "BridgedModule" in remote_name
            and "test_hook_import_top_level" in remote_name
        )

    @print_stats
    def test_hook_import_dotted(self):
        """ Test that we handle import x.y syntax """
        import test_hook_import_dotted.child

        remote_name = str(test_hook_import_dotted.child)
        self.assertTrue(
            "BridgedModule" in remote_name
            and "test_hook_import_dotted.child" in remote_name
        )

    @print_stats
    def test_hook_import_from_syntax(self):
        """ Test that we handle from x import y syntax """
        from test_hook_import_from import run_server

        remote_name = str(run_server)
        self.assertTrue(
            "BridgedCallable" in remote_name and "run_server" in remote_name
        )

    @print_stats
    def test_hook_import_nonexistent(self):
        """ Test that we handle a nonexistent import """
        with self.assertRaises(ImportError):
            import foobar

    @print_stats
    def test_hook_import_as(self):
        """ Test that we don't break import x as y syntax """
        import test_hook_import_as as thia

        remote_name = str(thia)
        self.assertTrue(
            "BridgedModule" in remote_name and "test_hook_import_as" in remote_name
        )

    @print_stats
    def test_hook_import_force_import(self):
        """ Test that we actually import something that's not loaded"""
        remote_sys = self.test_bridge.remote_import("sys")
        remote_python_version = remote_sys.version_info[0]
        local_python_version = sys.version_info[0]

        if local_python_version == 2 and remote_python_version == 3:
            # import a module in 3 that's not in 2
            # make sure it's not already loaded remotely
            self.assertTrue("http" not in remote_sys.modules)
            import http

            remote_name = str(http)
            self.assertTrue("BridgedModule" in remote_name and "http" in remote_name)

        elif local_python_version == 3 and remote_python_version == 2:
            # import a module in 2 that's not in 3
            # make sure it's not already loaded remotely
            self.assertTrue("SimpleHTTPServer" not in remote_sys.modules)
            import SimpleHTTPServer

            remote_name = str(SimpleHTTPServer)
            self.assertTrue(
                "BridgedModule" in remote_name and "SimpleHTTPServer" in remote_name
            )

        else:
            # same versions, can't think of anything useful to test load
            self.skipTest("Test irrelevant for matched versions")

    @print_stats
    def test_local_import(self):
        """ Make sure a local import is resolved locally, not pulled in remotely """
        self.assertTrue("ast" not in sys.modules)
        import ast

        name = str(ast)
        self.assertTrue("BridgedModule" not in name and "ast" in name)

    @print_stats
    def test_hook_import_nonmodule(self):
        """ Test we can import nonmodules like modules (e.g., java classes from jython). But mostly so we can test 
            reimporting
        """
        import test_hook_import_nonmodule

        remote_name = str(test_hook_import_nonmodule)
        self.assertTrue(
            "BridgedCallable" in remote_name and "run_server" in remote_name
        )


class TestBridgeHookImportReimport(unittest.TestCase):
    """ 
    Test the case of a separate client importing the same module as a previous client.
    Because the modules are only imported once in the server, if the first client sets objects on the remote module
    (e.g., __spec__), the second client will get old/unknown handle.
    
    Assumes there's a bridge server running at DEFAULT_SERVER_PORT.
    """

    @classmethod
    def setUpClass(cls):
        port = int(os.environ.get("TEST_PORT", bridge.DEFAULT_SERVER_PORT))
        old_importer_index = len(sys.path) - 1
        cls.test_bridge = bridge.BridgeClient(
            connect_to_port=port,
            loglevel=logging.DEBUG,
            hook_import=True,
            record_stats=True,
        )

        # rearrange paths to make sure our importer gets called first
        # TODO once we get around to implementing cleaning up import hooks on client shutdown, this shouldn't be required
        new_importer = sys.path[-1]
        old_importer = sys.path[old_importer_index]
        sys.path[old_importer_index] = new_importer
        sys.path[-1] = old_importer

    @print_stats
    def test_hook_import_nonmodule_again(self):
        """ If this fails with old/unknown handle, __spec__ has been set by the old client """
        # clear out our old import
        del sys.modules["test_hook_import_nonmodule"]

        import test_hook_import_nonmodule

        remote_name = str(test_hook_import_nonmodule)
        self.assertTrue(
            "BridgedCallable" in remote_name and "run_server" in remote_name
        )


class TestBridgeZZZZZZZShutdown(unittest.TestCase):
    """ Assumes there's a bridge server running at DEFAULT_SERVER_PORT. Needs to run last, nothing will work after this"""

    @classmethod
    def setUpClass(cls):
        port = int(os.environ.get("TEST_PORT", bridge.DEFAULT_SERVER_PORT))
        cls.test_bridge = bridge.BridgeClient(
            connect_to_port=port, loglevel=logging.DEBUG, record_stats=True
        )

    @print_stats
    def test_zzzzzz_shutdown(self):
        # test shutdown last
        result = self.test_bridge.remote_shutdown()
        self.assertTrue(result[bridge.SHUTDOWN])

        # give it a second to tear down
        time.sleep(1)

        # try to reconnect, should fail with connection refused
        with self.assertRaises(ConnectionRefusedError):
            fail_bridge = bridge.BridgeClient(
                connect_to_port=bridge.DEFAULT_SERVER_PORT, loglevel=logging.DEBUG
            )

            fail_bridge.remote_import("datetime")
