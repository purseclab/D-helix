#include <stdio.h>
 #include <stdbool.h>
 #include <stdint.h>
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    uint;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    uint;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned long    ulong;
typedef unsigned short    ushort;
typedef unsigned char    uchar;
typedef unsigned char   undefined;
typedef int code;
typedef float   float10;
unsigned short CONCAT11(unsigned char input1, unsigned char input2){
unsigned short concateresult = (((unsigned short) input1) << 8)  + (unsigned char)input2;
         return concateresult;
}
unsigned int CONCAT22(unsigned short input1, unsigned short input2){
unsigned int concateresult = (((unsigned int) input1) << 16)  + (unsigned short)input2;
         return concateresult;
}
unsigned long long CONCAT44(unsigned int input1, unsigned int input2){
unsigned long long concateresult = (((unsigned long long) input1) << 32)  + (unsigned int)input2;
         return concateresult;
}
__uint128_t  CONCAT88(unsigned long long input1, unsigned long long input2){
__uint128_t  concateresult = (((__uint128_t ) input1) << 64)  + (unsigned long long)input2;
         return concateresult;
}
unsigned char SEXT11(unsigned char input){
 unsigned b = 8;
unsigned char x = input;
unsigned char r;
unsigned char const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned char ZEXT11(unsigned char input){
 unsigned char output = ((unsigned char) ((unsigned char) input));
return output;
}
unsigned short SEXT12(unsigned char input){
 unsigned b = 8;
unsigned char x = input;
unsigned short r;
unsigned char const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned short ZEXT12(unsigned char input){
 unsigned short output = ((unsigned short) ((unsigned char) input));
return output;
}
unsigned int SEXT14(unsigned char input){
 unsigned b = 8;
unsigned char x = input;
unsigned int r;
unsigned char const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned int ZEXT14(unsigned char input){
 unsigned int output = ((unsigned int) ((unsigned char) input));
return output;
}
unsigned long long SEXT18(unsigned char input){
 unsigned b = 8;
unsigned char x = input;
unsigned long long r;
unsigned char const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned long long ZEXT18(unsigned char input){
 unsigned long long output = ((unsigned long long) ((unsigned char) input));
return output;
}
__uint128_t  SEXT116(unsigned char input){
 unsigned b = 8;
unsigned char x = input;
__uint128_t  r;
unsigned char const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
__uint128_t  ZEXT116(unsigned char input){
 __uint128_t  output = ((__uint128_t ) ((unsigned char) input));
return output;
}
unsigned short SEXT22(unsigned short input){
 unsigned b = 16;
unsigned short x = input;
unsigned short r;
unsigned short const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned short ZEXT22(unsigned short input){
 unsigned short output = ((unsigned short) ((unsigned short) input));
return output;
}
unsigned int SEXT24(unsigned short input){
 unsigned b = 16;
unsigned short x = input;
unsigned int r;
unsigned short const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned int ZEXT24(unsigned short input){
 unsigned int output = ((unsigned int) ((unsigned short) input));
return output;
}
unsigned long long SEXT28(unsigned short input){
 unsigned b = 16;
unsigned short x = input;
unsigned long long r;
unsigned short const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned long long ZEXT28(unsigned short input){
 unsigned long long output = ((unsigned long long) ((unsigned short) input));
return output;
}
__uint128_t  SEXT216(unsigned short input){
 unsigned b = 16;
unsigned short x = input;
__uint128_t  r;
unsigned short const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
__uint128_t  ZEXT216(unsigned short input){
 __uint128_t  output = ((__uint128_t ) ((unsigned short) input));
return output;
}
unsigned int SEXT44(unsigned int input){
 unsigned b = 32;
unsigned int x = input;
unsigned int r;
unsigned int const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned int ZEXT44(unsigned int input){
 unsigned int output = ((unsigned int) ((unsigned int) input));
return output;
}
unsigned long long SEXT48(unsigned int input){
 unsigned b = 32;
unsigned int x = input;
unsigned long long r;
unsigned int const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned long long ZEXT48(unsigned int input){
 unsigned long long output = ((unsigned long long) ((unsigned int) input));
return output;
}
__uint128_t  SEXT416(unsigned int input){
 unsigned b = 32;
unsigned int x = input;
__uint128_t  r;
unsigned int const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
__uint128_t  ZEXT416(unsigned int input){
 __uint128_t  output = ((__uint128_t ) ((unsigned int) input));
return output;
}
unsigned long long SEXT88(unsigned long long input){
 unsigned b = 64;
unsigned long long x = input;
unsigned long long r;
unsigned long long const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
unsigned long long ZEXT88(unsigned long long input){
 unsigned long long output = ((unsigned long long) ((unsigned long long) input));
return output;
}
__uint128_t  SEXT816(unsigned long long input){
 unsigned b = 64;
unsigned long long x = input;
__uint128_t  r;
unsigned long long const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
__uint128_t  ZEXT816(unsigned long long input){
 __uint128_t  output = ((__uint128_t ) ((unsigned long long) input));
return output;
}
__uint128_t  SEXT1616(__uint128_t  input){
 unsigned b = 128;
__uint128_t  x = input;
__uint128_t  r;
__uint128_t  const m = 1U << (b - 1);
x = x & ((1U << b) - 1);
r = (x ^ m) - m;
return r;
}
__uint128_t  ZEXT1616(__uint128_t  input){
 __uint128_t  output = ((__uint128_t ) ((__uint128_t ) input));
return output;
}
__uint128_t  SUB1616 (__uint128_t  input, int index){
__uint128_t  result = (input >> (8 * index));
return result;
}
unsigned long long SUB168 (__uint128_t  input, int index){
unsigned long long result = (input >> (8 * index));
return result;
}
unsigned int SUB164 (__uint128_t  input, int index){
unsigned int result = (input >> (8 * index));
return result;
}
unsigned short SUB162 (__uint128_t  input, int index){
unsigned short result = (input >> (8 * index));
return result;
}
unsigned char SUB161 (__uint128_t  input, int index){
unsigned char result = (input >> (8 * index));
return result;
}
unsigned long long SUB88 (unsigned long long input, int index){
unsigned long long result = (input >> (8 * index));
return result;
}
unsigned int SUB84 (unsigned long long input, int index){
unsigned int result = (input >> (8 * index));
return result;
}
unsigned short SUB82 (unsigned long long input, int index){
unsigned short result = (input >> (8 * index));
return result;
}
unsigned char SUB81 (unsigned long long input, int index){
unsigned char result = (input >> (8 * index));
return result;
}
unsigned int SUB44 (unsigned int input, int index){
unsigned int result = (input >> (8 * index));
return result;
}
unsigned short SUB42 (unsigned int input, int index){
unsigned short result = (input >> (8 * index));
return result;
}
unsigned char SUB41 (unsigned int input, int index){
unsigned char result = (input >> (8 * index));
return result;
}
unsigned short SUB22 (unsigned short input, int index){
unsigned short result = (input >> (8 * index));
return result;
}
unsigned char SUB21 (unsigned short input, int index){
unsigned char result = (input >> (8 * index));
return result;
}
unsigned char SUB11 (unsigned char input, int index){
unsigned char result = (input >> (8 * index));
return result;
}
typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned char    uchar;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned long long    ulonglong;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined3;
typedef unsigned int    undefined4;
typedef unsigned long    undefined5;
typedef unsigned long    undefined7;
typedef unsigned long    undefined8;
typedef unsigned short    ushort;
typedef unsigned short    word;
typedef struct eh_frame_hdr eh_frame_hdr, *Peh_frame_hdr;

struct eh_frame_hdr {
    byte eh_frame_hdr_version; // Exception Handler Frame Header Version
    dwfenc eh_frame_pointer_encoding; // Exception Handler Frame Pointer Encoding
    dwfenc eh_frame_desc_entry_count_encoding; // Encoding of # of Exception Handler FDEs
    dwfenc eh_frame_table_encoding; // Exception Handler Table Encoding
};

typedef struct fde_table_entry fde_table_entry, *Pfde_table_entry;

struct fde_table_entry {
    dword initial_loc; // Initial Location
    dword data_loc; // Data location
};

typedef struct termios termios, *Ptermios;

typedef uint tcflag_t;

typedef uchar cc_t;

typedef uint speed_t;

struct termios {
    tcflag_t c_iflag;
    tcflag_t c_oflag;
    tcflag_t c_cflag;
    tcflag_t c_lflag;
    cc_t c_line;
    cc_t c_cc[32];
    speed_t c_ispeed;
    speed_t c_ospeed;
};

typedef struct stat stat, *Pstat;

typedef ulong __dev_t;

typedef ulong __ino_t;

typedef ulong __nlink_t;

typedef uint __mode_t;

typedef uint __uid_t;

typedef uint __gid_t;

typedef long __off_t;

typedef long __blksize_t;

typedef long __blkcnt_t;

typedef struct timespec timespec, *Ptimespec;

typedef long __time_t;

struct timespec {
    __time_t tv_sec;
    long tv_nsec;
};

struct stat {
    __dev_t st_dev;
    __ino_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    long __unused[3];
};

typedef struct utsname utsname, *Putsname;

struct utsname {
    char sysname[65];
    char nodename[65];
    char release[65];
    char version[65];
    char machine[65];
    char domainname[65];
};

typedef struct hmac_ctx_st hmac_ctx_st, *Phmac_ctx_st;

typedef struct hmac_ctx_st HMAC_CTX;

typedef struct env_md_st env_md_st, *Penv_md_st;

typedef struct env_md_ctx_st env_md_ctx_st, *Penv_md_ctx_st;

typedef ulong size_t;

typedef struct env_md_ctx_st EVP_MD_CTX;

typedef struct env_md_st EVP_MD;

typedef struct engine_st engine_st, *Pengine_st;

typedef struct engine_st ENGINE;

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

struct engine_st {
};

struct env_md_ctx_st {
    EVP_MD * digest;
    ENGINE * engine;
    ulong flags;
    void * md_data;
    EVP_PKEY_CTX * pctx;
    int (* update)(EVP_MD_CTX *, void *, size_t);
};

struct evp_pkey_ctx_st {
};

struct hmac_ctx_st {
    EVP_MD * md;
    EVP_MD_CTX md_ctx;
    EVP_MD_CTX i_ctx;
    EVP_MD_CTX o_ctx;
    uint key_length;
    uchar key[128];
};

struct env_md_st {
    int type;
    int pkey_type;
    int md_size;
    ulong flags;
    int (* init)(EVP_MD_CTX *);
    int (* update)(EVP_MD_CTX *, void *, size_t);
    int (* final)(EVP_MD_CTX *, uchar *);
    int (* copy)(EVP_MD_CTX *, EVP_MD_CTX *);
    int (* cleanup)(EVP_MD_CTX *);
    int (* sign)(int, uchar *, uint, uchar *, uint *, void *);
    int (* verify)(int, uchar *, uint, uchar *, uint, void *);
    int required_pkey_type[5];
    int block_size;
    int ctx_size;
    int (* md_ctrl)(EVP_MD_CTX *, int, int, void *);
};

typedef struct cast_key_st cast_key_st, *Pcast_key_st;

struct cast_key_st {
    uint data[32];
    int short_key;
};

typedef struct cast_key_st CAST_KEY;

typedef struct CMAC_CTX_st CMAC_CTX_st, *PCMAC_CTX_st;

struct CMAC_CTX_st {
};

typedef struct cert_st cert_st, *Pcert_st;

struct cert_st {
};

typedef struct srtp_protection_profile_st srtp_protection_profile_st, *Psrtp_protection_profile_st;

struct srtp_protection_profile_st {
    char * name;
    ulong id;
};

typedef struct ssl_session_st ssl_session_st, *Pssl_session_st;

typedef struct sess_cert_st sess_cert_st, *Psess_cert_st;

typedef struct x509_st x509_st, *Px509_st;

typedef struct x509_st X509;

typedef struct ssl_cipher_st ssl_cipher_st, *Pssl_cipher_st;

typedef struct ssl_cipher_st SSL_CIPHER;

typedef struct stack_st_SSL_CIPHER stack_st_SSL_CIPHER, *Pstack_st_SSL_CIPHER;

typedef struct crypto_ex_data_st crypto_ex_data_st, *Pcrypto_ex_data_st;

typedef struct crypto_ex_data_st CRYPTO_EX_DATA;

typedef struct x509_cinf_st x509_cinf_st, *Px509_cinf_st;

typedef struct x509_cinf_st X509_CINF;

typedef struct X509_algor_st X509_algor_st, *PX509_algor_st;

typedef struct X509_algor_st X509_ALGOR;

typedef struct asn1_string_st asn1_string_st, *Pasn1_string_st;

typedef struct asn1_string_st ASN1_BIT_STRING;

typedef struct asn1_string_st ASN1_OCTET_STRING;

typedef struct AUTHORITY_KEYID_st AUTHORITY_KEYID_st, *PAUTHORITY_KEYID_st;

typedef struct AUTHORITY_KEYID_st AUTHORITY_KEYID;

typedef struct X509_POLICY_CACHE_st X509_POLICY_CACHE_st, *PX509_POLICY_CACHE_st;

typedef struct X509_POLICY_CACHE_st X509_POLICY_CACHE;

typedef struct stack_st_DIST_POINT stack_st_DIST_POINT, *Pstack_st_DIST_POINT;

typedef struct stack_st_GENERAL_NAME stack_st_GENERAL_NAME, *Pstack_st_GENERAL_NAME;

typedef struct NAME_CONSTRAINTS_st NAME_CONSTRAINTS_st, *PNAME_CONSTRAINTS_st;

typedef struct NAME_CONSTRAINTS_st NAME_CONSTRAINTS;

typedef struct stack_st_IPAddressFamily stack_st_IPAddressFamily, *Pstack_st_IPAddressFamily;

typedef struct ASIdentifiers_st ASIdentifiers_st, *PASIdentifiers_st;

typedef struct x509_cert_aux_st x509_cert_aux_st, *Px509_cert_aux_st;

typedef struct x509_cert_aux_st X509_CERT_AUX;

typedef struct stack_st stack_st, *Pstack_st;

typedef struct stack_st _STACK;

typedef struct stack_st_void stack_st_void, *Pstack_st_void;

typedef struct asn1_string_st ASN1_INTEGER;

typedef struct X509_name_st X509_name_st, *PX509_name_st;

typedef struct X509_name_st X509_NAME;

typedef struct X509_val_st X509_val_st, *PX509_val_st;

typedef struct X509_val_st X509_VAL;

typedef struct X509_pubkey_st X509_pubkey_st, *PX509_pubkey_st;

typedef struct X509_pubkey_st X509_PUBKEY;

typedef struct stack_st_X509_EXTENSION stack_st_X509_EXTENSION, *Pstack_st_X509_EXTENSION;

typedef struct ASN1_ENCODING_st ASN1_ENCODING_st, *PASN1_ENCODING_st;

typedef struct ASN1_ENCODING_st ASN1_ENCODING;

typedef struct asn1_object_st asn1_object_st, *Pasn1_object_st;

typedef struct asn1_object_st ASN1_OBJECT;

typedef struct asn1_type_st asn1_type_st, *Pasn1_type_st;

typedef struct asn1_type_st ASN1_TYPE;

typedef struct stack_st_GENERAL_NAME GENERAL_NAMES;

typedef struct stack_st_GENERAL_SUBTREE stack_st_GENERAL_SUBTREE, *Pstack_st_GENERAL_SUBTREE;

typedef struct ASIdentifierChoice_st ASIdentifierChoice_st, *PASIdentifierChoice_st;

typedef struct ASIdentifierChoice_st ASIdentifierChoice;

typedef struct stack_st_ASN1_OBJECT stack_st_ASN1_OBJECT, *Pstack_st_ASN1_OBJECT;

typedef struct asn1_string_st ASN1_UTF8STRING;

typedef struct stack_st_X509_ALGOR stack_st_X509_ALGOR, *Pstack_st_X509_ALGOR;

typedef struct stack_st_X509_NAME_ENTRY stack_st_X509_NAME_ENTRY, *Pstack_st_X509_NAME_ENTRY;

typedef struct buf_mem_st buf_mem_st, *Pbuf_mem_st;

typedef struct buf_mem_st BUF_MEM;

typedef struct asn1_string_st ASN1_TIME;

typedef struct evp_pkey_st evp_pkey_st, *Pevp_pkey_st;

typedef struct evp_pkey_st EVP_PKEY;

typedef union _union_257 _union_257, *P_union_257;

typedef union _union_930 _union_930, *P_union_930;

typedef struct evp_pkey_asn1_method_st evp_pkey_asn1_method_st, *Pevp_pkey_asn1_method_st;

typedef struct evp_pkey_asn1_method_st EVP_PKEY_ASN1_METHOD;

typedef union _union_271 _union_271, *P_union_271;

typedef struct stack_st_X509_ATTRIBUTE stack_st_X509_ATTRIBUTE, *Pstack_st_X509_ATTRIBUTE;

typedef int ASN1_BOOLEAN;

typedef struct asn1_string_st ASN1_STRING;

typedef struct asn1_string_st ASN1_ENUMERATED;

typedef struct asn1_string_st ASN1_PRINTABLESTRING;

typedef struct asn1_string_st ASN1_T61STRING;

typedef struct asn1_string_st ASN1_IA5STRING;

typedef struct asn1_string_st ASN1_GENERALSTRING;

typedef struct asn1_string_st ASN1_BMPSTRING;

typedef struct asn1_string_st ASN1_UNIVERSALSTRING;

typedef struct asn1_string_st ASN1_UTCTIME;

typedef struct asn1_string_st ASN1_GENERALIZEDTIME;

typedef struct asn1_string_st ASN1_VISIBLESTRING;

typedef struct ASN1_VALUE_st ASN1_VALUE_st, *PASN1_VALUE_st;

typedef struct ASN1_VALUE_st ASN1_VALUE;

typedef int ASN1_NULL;

typedef struct stack_st_ASIdOrRange stack_st_ASIdOrRange, *Pstack_st_ASIdOrRange;

typedef struct stack_st_ASIdOrRange ASIdOrRanges;

typedef struct rsa_st rsa_st, *Prsa_st;

typedef struct dsa_st dsa_st, *Pdsa_st;

typedef struct dh_st dh_st, *Pdh_st;

typedef struct ec_key_st ec_key_st, *Pec_key_st;

typedef struct rsa_meth_st rsa_meth_st, *Prsa_meth_st;

typedef struct rsa_st RSA;

typedef struct bignum_st bignum_st, *Pbignum_st;

typedef struct bignum_st BIGNUM;

typedef struct bignum_ctx bignum_ctx, *Pbignum_ctx;

typedef struct bignum_ctx BN_CTX;

typedef struct bn_mont_ctx_st bn_mont_ctx_st, *Pbn_mont_ctx_st;

typedef struct bn_mont_ctx_st BN_MONT_CTX;

typedef struct bn_gencb_st bn_gencb_st, *Pbn_gencb_st;

typedef struct bn_gencb_st BN_GENCB;

typedef struct rsa_meth_st RSA_METHOD;

typedef struct bn_blinding_st bn_blinding_st, *Pbn_blinding_st;

typedef struct bn_blinding_st BN_BLINDING;

typedef struct dsa_method dsa_method, *Pdsa_method;

typedef struct DSA_SIG_st DSA_SIG_st, *PDSA_SIG_st;

typedef struct DSA_SIG_st DSA_SIG;

typedef struct dsa_st DSA;

typedef struct dsa_method DSA_METHOD;

typedef struct dh_method dh_method, *Pdh_method;

typedef struct dh_st DH;

typedef struct dh_method DH_METHOD;

typedef union _union_175 _union_175, *P_union_175;

struct crypto_ex_data_st {
    struct stack_st_void * sk;
    int dummy;
};

struct stack_st {
    int num;
    char * * data;
    int sorted;
    int num_alloc;
    int (* comp)(void *, void *);
};

struct stack_st_SSL_CIPHER {
    _STACK stack;
};

struct ssl_cipher_st {
    int valid;
    char * name;
    ulong id;
    ulong algorithm_mkey;
    ulong algorithm_auth;
    ulong algorithm_enc;
    ulong algorithm_mac;
    ulong algorithm_ssl;
    ulong algo_strength;
    ulong algorithm2;
    int strength_bits;
    int alg_bits;
};

struct evp_pkey_asn1_method_st {
};

struct X509_pubkey_st {
    X509_ALGOR * algor;
    ASN1_BIT_STRING * public_key;
    EVP_PKEY * pkey;
};

union _union_257 {
    char * ptr;
    ASN1_BOOLEAN boolean;
    ASN1_STRING * asn1_string;
    ASN1_OBJECT * object;
    ASN1_INTEGER * integer;
    ASN1_ENUMERATED * enumerated;
    ASN1_BIT_STRING * bit_string;
    ASN1_OCTET_STRING * octet_string;
    ASN1_PRINTABLESTRING * printablestring;
    ASN1_T61STRING * t61string;
    ASN1_IA5STRING * ia5string;
    ASN1_GENERALSTRING * generalstring;
    ASN1_BMPSTRING * bmpstring;
    ASN1_UNIVERSALSTRING * universalstring;
    ASN1_UTCTIME * utctime;
    ASN1_GENERALIZEDTIME * generalizedtime;
    ASN1_VISIBLESTRING * visiblestring;
    ASN1_UTF8STRING * utf8string;
    ASN1_STRING * set;
    ASN1_STRING * sequence;
    ASN1_VALUE * asn1_value;
};

struct asn1_type_st {
    int type;
    union _union_257 value;
};

struct dh_method {
    char * name;
    int (* generate_key)(DH *);
    int (* compute_key)(uchar *, BIGNUM *, DH *);
    int (* bn_mod_exp)(DH *, BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);
    int (* init)(DH *);
    int (* finish)(DH *);
    int flags;
    char * app_data;
    int (* generate_params)(DH *, int, int, BN_GENCB *);
};

struct buf_mem_st {
    size_t length;
    char * data;
    size_t max;
};

struct stack_st_X509_ATTRIBUTE {
    _STACK stack;
};

struct NAME_CONSTRAINTS_st {
    struct stack_st_GENERAL_SUBTREE * permittedSubtrees;
    struct stack_st_GENERAL_SUBTREE * excludedSubtrees;
};

struct stack_st_void {
    _STACK stack;
};

struct ASN1_VALUE_st {
};

struct x509_st {
    X509_CINF * cert_info;
    X509_ALGOR * sig_alg;
    ASN1_BIT_STRING * signature;
    int valid;
    int references;
    char * name;
    CRYPTO_EX_DATA ex_data;
    long ex_pathlen;
    long ex_pcpathlen;
    ulong ex_flags;
    ulong ex_kusage;
    ulong ex_xkusage;
    ulong ex_nscert;
    ASN1_OCTET_STRING * skid;
    AUTHORITY_KEYID * akid;
    X509_POLICY_CACHE * policy_cache;
    struct stack_st_DIST_POINT * crldp;
    struct stack_st_GENERAL_NAME * altname;
    NAME_CONSTRAINTS * nc;
    struct stack_st_IPAddressFamily * rfc3779_addr;
    struct ASIdentifiers_st * rfc3779_asid;
    uchar sha1_hash[20];
    X509_CERT_AUX * aux;
};

struct dsa_st {
    int pad;
    long version;
    int write_params;
    BIGNUM * p;
    BIGNUM * q;
    BIGNUM * g;
    BIGNUM * pub_key;
    BIGNUM * priv_key;
    BIGNUM * kinv;
    BIGNUM * r;
    int flags;
    BN_MONT_CTX * method_mont_p;
    int references;
    CRYPTO_EX_DATA ex_data;
    DSA_METHOD * meth;
    ENGINE * engine;
};

struct stack_st_ASN1_OBJECT {
    _STACK stack;
};

struct asn1_object_st {
    char * sn;
    char * * ln;
    int nid;
    int length;
    uchar * data;
    int flags;
};

struct ASN1_ENCODING_st {
    uchar * enc;
    long len;
    int modified;
};

struct stack_st_GENERAL_SUBTREE {
    _STACK stack;
};

struct bignum_st {
    ulong * d;
    int top;
    int dmax;
    int neg;
    int flags;
};

struct rsa_meth_st {
    char * name;
    int (* rsa_pub_enc)(int, uchar *, uchar *, RSA *, int);
    int (* rsa_pub_dec)(int, uchar *, uchar *, RSA *, int);
    int (* rsa_priv_enc)(int, uchar *, uchar *, RSA *, int);
    int (* rsa_priv_dec)(int, uchar *, uchar *, RSA *, int);
    int (* rsa_mod_exp)(BIGNUM *, BIGNUM *, RSA *, BN_CTX *);
    int (* bn_mod_exp)(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);
    int (* init)(RSA *);
    int (* finish)(RSA *);
    int flags;
    char * app_data;
    int (* rsa_sign)(int, uchar *, uint, uchar *, uint *, RSA *);
    int (* rsa_verify)(int, uchar *, uint, uchar *, uint, RSA *);
    int (* rsa_keygen)(RSA *, int, BIGNUM *, BN_GENCB *);
};

union _union_175 {
    void (* cb_1)(int, int, void *);
    int (* cb_2)(int, int, BN_GENCB *);
};

struct asn1_string_st {
    int length;
    int type;
    uchar * data;
    long flags;
};

struct stack_st_GENERAL_NAME {
    _STACK stack;
};

union _union_930 {
    ASN1_NULL * inherit;
    ASIdOrRanges * asIdsOrRanges;
};

struct bn_gencb_st {
    uint ver;
    void * arg;
    union _union_175 cb;
};

union _union_271 {
    char * ptr;
    struct rsa_st * rsa;
    struct dsa_st * dsa;
    struct dh_st * dh;
    struct ec_key_st * ec;
};

struct x509_cinf_st {
    ASN1_INTEGER * version;
    ASN1_INTEGER * serialNumber;
    X509_ALGOR * signature;
    X509_NAME * issuer;
    X509_VAL * validity;
    X509_NAME * subject;
    X509_PUBKEY * key;
    ASN1_BIT_STRING * issuerUID;
    ASN1_BIT_STRING * subjectUID;
    struct stack_st_X509_EXTENSION * extensions;
    ASN1_ENCODING enc;
};

struct rsa_st {
    int pad;
    long version;
    RSA_METHOD * meth;
    ENGINE * engine;
    BIGNUM * n;
    BIGNUM * e;
    BIGNUM * d;
    BIGNUM * p;
    BIGNUM * q;
    BIGNUM * dmp1;
    BIGNUM * dmq1;
    BIGNUM * iqmp;
    CRYPTO_EX_DATA ex_data;
    int references;
    int flags;
    BN_MONT_CTX * _method_mod_n;
    BN_MONT_CTX * _method_mod_p;
    BN_MONT_CTX * _method_mod_q;
    char * bignum_data;
    BN_BLINDING * blinding;
    BN_BLINDING * mt_blinding;
};

struct stack_st_X509_ALGOR {
    _STACK stack;
};

struct dh_st {
    int pad;
    int version;
    BIGNUM * p;
    BIGNUM * g;
    long length;
    BIGNUM * pub_key;
    BIGNUM * priv_key;
    int flags;
    BN_MONT_CTX * method_mont_p;
    BIGNUM * q;
    BIGNUM * j;
    uchar * seed;
    int seedlen;
    BIGNUM * counter;
    int references;
    CRYPTO_EX_DATA ex_data;
    DH_METHOD * meth;
    ENGINE * engine;
};

struct AUTHORITY_KEYID_st {
    ASN1_OCTET_STRING * keyid;
    GENERAL_NAMES * issuer;
    ASN1_INTEGER * serial;
};

struct bn_blinding_st {
};

struct stack_st_DIST_POINT {
    _STACK stack;
};

struct ec_key_st {
};

struct ASIdentifiers_st {
    ASIdentifierChoice * asnum;
    ASIdentifierChoice * * rdi;
};

struct X509_name_st {
    struct stack_st_X509_NAME_ENTRY * entries;
    int modified;
    BUF_MEM * bytes;
    uchar * canon_enc;
    int canon_enclen;
};

struct X509_algor_st {
    ASN1_OBJECT * algorithm;
    ASN1_TYPE * parameter;
};

struct ssl_session_st {
    int ssl_version;
    uint key_arg_length;
    uchar key_arg[8];
    int master_key_length;
    uchar master_key[48];
    uint session_id_length;
    uchar session_id[32];
    uint sid_ctx_length;
    uchar sid_ctx[32];
    uint krb5_client_princ_len;
    uchar krb5_client_princ[256];
    char * psk_identity_hint;
    char * psk_identity;
    int not_resumable;
    struct sess_cert_st * sess_cert;
    X509 * peer;
    long verify_result;
    int references;
    long timeout;
    long time;
    uint compress_meth;
    SSL_CIPHER * cipher;
    ulong cipher_id;
    struct stack_st_SSL_CIPHER * ciphers;
    CRYPTO_EX_DATA ex_data;
    struct ssl_session_st * prev;
    struct ssl_session_st * * next;
    char * tlsext_hostname;
    size_t tlsext_ecpointformatlist_length;
    uchar * tlsext_ecpointformatlist;
    size_t tlsext_ellipticcurvelist_length;
    uchar * tlsext_ellipticcurvelist;
    uchar * tlsext_tick;
    size_t tlsext_ticklen;
    long tlsext_tick_lifetime_hint;
};

struct X509_val_st {
    ASN1_TIME * notBefore;
    ASN1_TIME * notAfter;
};

struct bignum_ctx {
};

struct stack_st_X509_EXTENSION {
    _STACK stack;
};

struct DSA_SIG_st {
    BIGNUM * r;
    BIGNUM * s;
};

struct X509_POLICY_CACHE_st {
};

struct stack_st_IPAddressFamily {
    _STACK stack;
};

struct stack_st_ASIdOrRange {
    _STACK stack;
};

struct x509_cert_aux_st {
    struct stack_st_ASN1_OBJECT * trust;
    struct stack_st_ASN1_OBJECT * reject;
    ASN1_UTF8STRING * alias;
    ASN1_OCTET_STRING * keyid;
    struct stack_st_X509_ALGOR * other;
};

struct ASIdentifierChoice_st {
    int type;
    union _union_930 u;
};

struct stack_st_X509_NAME_ENTRY {
    _STACK stack;
};

struct dsa_method {
    char * name;
    DSA_SIG * (* dsa_do_sign)(uchar *, int, DSA *);
    int (* dsa_sign_setup)(DSA *, BN_CTX *, BIGNUM * *, BIGNUM * *);
    int (* dsa_do_verify)(uchar *, int, DSA_SIG *, DSA *);
    int (* dsa_mod_exp)(DSA *, BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);
    int (* bn_mod_exp)(DSA *, BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);
    int (* init)(DSA *);
    int (* finish)(DSA *);
    int flags;
    char * app_data;
    int (* dsa_paramgen)(DSA *, int, uchar *, int, int *, ulong *, BN_GENCB *);
    int (* dsa_keygen)(DSA *);
};

struct evp_pkey_st {
    int type;
    int save_type;
    int references;
    EVP_PKEY_ASN1_METHOD * ameth;
    ENGINE * engine;
    union _union_271 pkey;
    int save_parameters;
    struct stack_st_X509_ATTRIBUTE * attributes;
};

struct sess_cert_st {
};

struct bn_mont_ctx_st {
    int ri;
    BIGNUM RR;
    BIGNUM N;
    BIGNUM Ni;
    ulong n0[2];
    int flags;
};

typedef struct lhash_st_SSL_SESSION lhash_st_SSL_SESSION, *Plhash_st_SSL_SESSION;

struct lhash_st_SSL_SESSION {
    int dummy;
};

typedef struct ssl_comp_st ssl_comp_st, *Pssl_comp_st;

typedef struct comp_method_st comp_method_st, *Pcomp_method_st;

typedef struct comp_ctx_st comp_ctx_st, *Pcomp_ctx_st;

typedef struct comp_ctx_st COMP_CTX;

typedef struct comp_method_st COMP_METHOD;

struct ssl_comp_st {
    int id;
    char * name;
    COMP_METHOD * method;
};

struct comp_ctx_st {
    COMP_METHOD * meth;
    ulong compress_in;
    ulong compress_out;
    ulong expand_in;
    ulong expand_out;
    CRYPTO_EX_DATA ex_data;
};

struct comp_method_st {
    int type;
    char * name;
    int (* init)(COMP_CTX *);
    void (* finish)(COMP_CTX *);
    int (* compress)(COMP_CTX *, uchar *, uint, uchar *, uint);
    int (* expand)(COMP_CTX *, uchar *, uint, uchar *, uint);
    long (* ctrl)(void);
    long (* callback_ctrl)(void);
};

typedef struct ssl3_buf_freelist_st ssl3_buf_freelist_st, *Pssl3_buf_freelist_st;

struct ssl3_buf_freelist_st {
};

typedef struct stack_st_SRTP_PROTECTION_PROFILE stack_st_SRTP_PROTECTION_PROFILE, *Pstack_st_SRTP_PROTECTION_PROFILE;

struct stack_st_SRTP_PROTECTION_PROFILE {
    _STACK stack;
};

typedef struct ssl_comp_st SSL_COMP;

typedef struct ssl3_enc_method ssl3_enc_method, *Pssl3_enc_method;

struct ssl3_enc_method {
};

typedef struct ssl3_state_st ssl3_state_st, *Pssl3_state_st;

typedef struct ssl3_buffer_st ssl3_buffer_st, *Pssl3_buffer_st;

typedef struct ssl3_buffer_st SSL3_BUFFER;

typedef struct ssl3_record_st ssl3_record_st, *Pssl3_record_st;

typedef struct ssl3_record_st SSL3_RECORD;

typedef struct bio_st bio_st, *Pbio_st;

typedef struct bio_st BIO;

typedef struct _struct_645 _struct_645, *P_struct_645;

typedef struct bio_method_st bio_method_st, *Pbio_method_st;

typedef void (bio_info_cb)(struct bio_st *, int, char *, int, long, long);

typedef struct bio_method_st BIO_METHOD;

typedef struct ec_key_st EC_KEY;

typedef struct stack_st_X509_NAME stack_st_X509_NAME, *Pstack_st_X509_NAME;

typedef struct evp_cipher_st evp_cipher_st, *Pevp_cipher_st;

typedef struct evp_cipher_ctx_st evp_cipher_ctx_st, *Pevp_cipher_ctx_st;

typedef struct evp_cipher_ctx_st EVP_CIPHER_CTX;

typedef struct evp_cipher_st EVP_CIPHER;

struct ssl3_record_st {
    int type;
    uint length;
    uint off;
    uchar * data;
    uchar * input;
    uchar * comp;
    ulong epoch;
    uchar seq_num[8];
};

struct evp_cipher_st {
    int nid;
    int block_size;
    int key_len;
    int iv_len;
    ulong flags;
    int (* init)(EVP_CIPHER_CTX *, uchar *, uchar *, int);
    int (* do_cipher)(EVP_CIPHER_CTX *, uchar *, uchar *, size_t);
    int (* cleanup)(EVP_CIPHER_CTX *);
    int ctx_size;
    int (* set_asn1_parameters)(EVP_CIPHER_CTX *, ASN1_TYPE *);
    int (* get_asn1_parameters)(EVP_CIPHER_CTX *, ASN1_TYPE *);
    int (* ctrl)(EVP_CIPHER_CTX *, int, int, void *);
    void * app_data;
};

struct _struct_645 {
    uchar cert_verify_md[128];
    uchar finish_md[128];
    int finish_md_len;
    uchar peer_finish_md[128];
    int peer_finish_md_len;
    ulong message_size;
    int message_type;
    SSL_CIPHER * new_cipher;
    DH * dh;
    EC_KEY * ecdh;
    int next_state;
    int reuse_message;
    int cert_req;
    int ctype_num;
    char ctype[9];
    struct stack_st_X509_NAME * ca_names;
    int use_rsa_tmp;
    int key_block_length;
    uchar * key_block;
    EVP_CIPHER * new_sym_enc;
    EVP_MD * new_hash;
    int new_mac_pkey_type;
    int new_mac_secret_size;
    SSL_COMP * new_compression;
    int cert_request;
};

struct ssl3_buffer_st {
    uchar * buf;
    size_t len;
    int offset;
    int left;
};

struct bio_st {
    BIO_METHOD * method;
    long (* callback)(struct bio_st *, int, char *, int, long, long);
    char * cb_arg;
    int init;
    int shutdown;
    int flags;
    int retry_reason;
    int num;
    void * ptr;
    struct bio_st * next_bio;
    struct bio_st * prev_bio;
    int references;
    ulong num_read;
    ulong num_write;
    CRYPTO_EX_DATA ex_data;
};

struct ssl3_state_st {
    long flags;
    int delay_buf_pop_ret;
    uchar read_sequence[8];
    int read_mac_secret_size;
    uchar read_mac_secret[64];
    uchar write_sequence[8];
    int write_mac_secret_size;
    uchar write_mac_secret[64];
    uchar server_random[32];
    uchar client_random[32];
    int need_empty_fragments;
    int empty_fragment_done;
    int init_extra;
    SSL3_BUFFER rbuf;
    SSL3_BUFFER wbuf;
    SSL3_RECORD rrec;
    SSL3_RECORD wrec;
    uchar alert_fragment[2];
    uint alert_fragment_len;
    uchar handshake_fragment[4];
    uint handshake_fragment_len;
    uint wnum;
    int wpend_tot;
    int wpend_type;
    int wpend_ret;
    uchar * wpend_buf;
    BIO * handshake_buffer;
    EVP_MD_CTX * * handshake_dgst;
    int change_cipher_spec;
    int warn_alert;
    int fatal_alert;
    int alert_dispatch;
    uchar send_alert[2];
    int renegotiate;
    int total_renegotiations;
    int num_renegotiations;
    int in_read_app_data;
    void * client_opaque_prf_input;
    size_t client_opaque_prf_input_len;
    void * server_opaque_prf_input;
    size_t server_opaque_prf_input_len;
    struct _struct_645 tmp;
    uchar previous_client_finished[64];
    uchar previous_client_finished_len;
    uchar previous_server_finished[64];
    uchar previous_server_finished_len;
    int send_connection_binding;
    int next_proto_neg_seen;
};

struct stack_st_X509_NAME {
    _STACK stack;
};

struct evp_cipher_ctx_st {
    EVP_CIPHER * cipher;
    ENGINE * engine;
    int encrypt;
    int buf_len;
    uchar oiv[16];
    uchar iv[16];
    uchar buf[32];
    int num;
    void * app_data;
    int key_len;
    ulong flags;
    void * cipher_data;
    int final_used;
    int block_mask;
    uchar final[32];
};

struct bio_method_st {
    int type;
    char * name;
    int (* bwrite)(BIO *, char *, int);
    int (* bread)(BIO *, char *, int);
    int (* bputs)(BIO *, char *);
    int (* bgets)(BIO *, char *, int);
    long (* ctrl)(BIO *, int, long, void *);
    int (* create)(BIO *);
    int (* destroy)(BIO *);
    long (* callback_ctrl)(BIO *, int, bio_info_cb *);
};

typedef struct srtp_protection_profile_st SRTP_PROTECTION_PROFILE;

typedef struct stack_st_OCSP_RESPID stack_st_OCSP_RESPID, *Pstack_st_OCSP_RESPID;

struct stack_st_OCSP_RESPID {
    _STACK stack;
};

typedef struct ssl2_state_st ssl2_state_st, *Pssl2_state_st;

typedef struct _struct_641 _struct_641, *P_struct_641;

struct _struct_641 {
    uint conn_id_length;
    uint cert_type;
    uint cert_length;
    uint csl;
    uint clear;
    uint enc;
    uchar ccl[32];
    uint cipher_spec_length;
    uint session_id_length;
    uint clen;
    uint rlen;
};

struct ssl2_state_st {
    int three_byte_header;
    int clear_text;
    int escape;
    int ssl2_rollback;
    uint wnum;
    int wpend_tot;
    uchar * wpend_buf;
    int wpend_off;
    int wpend_len;
    int wpend_ret;
    int rbuf_left;
    int rbuf_offs;
    uchar * rbuf;
    uchar * wbuf;
    uchar * write_ptr;
    uint padding;
    uint rlength;
    int ract_data_length;
    uint wlength;
    int wact_data_length;
    uchar * ract_data;
    uchar * wact_data;
    uchar * mac_data;
    uchar * read_key;
    uchar * write_key;
    uint challenge_length;
    uchar challenge[32];
    uint conn_id_length;
    uchar conn_id[16];
    uint key_material_length;
    uchar key_material[48];
    ulong read_sequence;
    ulong write_sequence;
    struct _struct_641 tmp;
};

typedef struct tls_session_ticket_ext_st tls_session_ticket_ext_st, *Ptls_session_ticket_ext_st;

typedef struct tls_session_ticket_ext_st TLS_SESSION_TICKET_EXT;

struct tls_session_ticket_ext_st {
};

typedef struct ssl_method_st ssl_method_st, *Pssl_method_st;

typedef struct ssl_st ssl_st, *Pssl_st;

typedef struct x509_store_ctx_st x509_store_ctx_st, *Px509_store_ctx_st;

typedef struct X509_crl_st X509_crl_st, *PX509_crl_st;

typedef struct X509_crl_st X509_CRL;

typedef struct stack_st_X509 stack_st_X509, *Pstack_st_X509;

typedef struct stack_st_X509_CRL stack_st_X509_CRL, *Pstack_st_X509_CRL;

typedef struct x509_store_ctx_st X509_STORE_CTX;

typedef struct ssl_st SSL;

typedef struct ssl_ctx_st ssl_ctx_st, *Pssl_ctx_st;

typedef struct ssl_session_st SSL_SESSION;

typedef struct ssl_ctx_st SSL_CTX;

typedef struct ssl_method_st SSL_METHOD;

typedef struct dtls1_state_st dtls1_state_st, *Pdtls1_state_st;

typedef struct X509_VERIFY_PARAM_st X509_VERIFY_PARAM_st, *PX509_VERIFY_PARAM_st;

typedef struct X509_VERIFY_PARAM_st X509_VERIFY_PARAM;

typedef int (* GEN_SESSION_CB)(SSL *, uchar *, uint *);

typedef struct x509_store_st x509_store_st, *Px509_store_st;

typedef struct x509_store_st X509_STORE;

typedef struct X509_crl_info_st X509_crl_info_st, *PX509_crl_info_st;

typedef struct X509_crl_info_st X509_CRL_INFO;

typedef struct ISSUING_DIST_POINT_st ISSUING_DIST_POINT_st, *PISSUING_DIST_POINT_st;

typedef struct ISSUING_DIST_POINT_st ISSUING_DIST_POINT;

typedef struct stack_st_GENERAL_NAMES stack_st_GENERAL_NAMES, *Pstack_st_GENERAL_NAMES;

typedef struct x509_crl_method_st x509_crl_method_st, *Px509_crl_method_st;

typedef struct x509_crl_method_st X509_CRL_METHOD;

typedef struct X509_POLICY_TREE_st X509_POLICY_TREE_st, *PX509_POLICY_TREE_st;

typedef struct X509_POLICY_TREE_st X509_POLICY_TREE;

typedef struct kssl_ctx_st kssl_ctx_st, *Pkssl_ctx_st;

typedef struct kssl_ctx_st KSSL_CTX;

typedef struct stack_st_X509_EXTENSION X509_EXTENSIONS;

typedef int (* tls_session_ticket_ext_cb_fn)(SSL *, uchar *, int, void *);

typedef int (* tls_session_secret_cb_fn)(SSL *, void *, int *, struct stack_st_SSL_CIPHER *, SSL_CIPHER * *, void *);

typedef struct _struct_615 _struct_615, *P_struct_615;

typedef int (pem_password_cb)(char *, int, int, void *);

typedef struct stack_st_SSL_COMP stack_st_SSL_COMP, *Pstack_st_SSL_COMP;

typedef struct dtls1_bitmap_st dtls1_bitmap_st, *Pdtls1_bitmap_st;

typedef struct dtls1_bitmap_st DTLS1_BITMAP;

typedef struct record_pqueue_st record_pqueue_st, *Precord_pqueue_st;

typedef struct record_pqueue_st record_pqueue;

typedef struct _pqueue _pqueue, *P_pqueue;

typedef struct _pqueue * pqueue;

typedef struct hm_header_st hm_header_st, *Phm_header_st;

typedef struct dtls1_timeout_st dtls1_timeout_st, *Pdtls1_timeout_st;

typedef struct timeval timeval, *Ptimeval;

typedef __time_t time_t;

typedef struct stack_st_X509_OBJECT stack_st_X509_OBJECT, *Pstack_st_X509_OBJECT;

typedef struct stack_st_X509_LOOKUP stack_st_X509_LOOKUP, *Pstack_st_X509_LOOKUP;

typedef struct stack_st_X509_REVOKED stack_st_X509_REVOKED, *Pstack_st_X509_REVOKED;

typedef struct DIST_POINT_NAME_st DIST_POINT_NAME_st, *PDIST_POINT_NAME_st;

typedef struct DIST_POINT_NAME_st DIST_POINT_NAME;

typedef int krb5_int32;

typedef krb5_int32 krb5_enctype;

typedef uchar krb5_octet;

typedef struct dtls1_retransmit_state dtls1_retransmit_state, *Pdtls1_retransmit_state;

typedef long __suseconds_t;

typedef union _union_856 _union_856, *P_union_856;

struct record_pqueue_st {
    ushort epoch;
    pqueue q;
};

struct x509_crl_method_st {
};

struct dtls1_retransmit_state {
    EVP_CIPHER_CTX * enc_write_ctx;
    EVP_MD_CTX * write_hash;
    COMP_CTX * compress;
    SSL_SESSION * session;
    ushort epoch;
};

struct hm_header_st {
    uchar type;
    ulong msg_len;
    ushort seq;
    ulong frag_off;
    ulong frag_len;
    uint is_ccs;
    struct dtls1_retransmit_state saved_retransmit_state;
};

struct ISSUING_DIST_POINT_st {
    DIST_POINT_NAME * distpoint;
    int onlyuser;
    int onlyCA;
    ASN1_BIT_STRING * onlysomereasons;
    int indirectCRL;
    int onlyattr;
};

struct timeval {
    __time_t tv_sec;
    __suseconds_t tv_usec;
};

struct X509_crl_st {
    X509_CRL_INFO * crl;
    X509_ALGOR * sig_alg;
    ASN1_BIT_STRING * signature;
    int references;
    int flags;
    AUTHORITY_KEYID * akid;
    ISSUING_DIST_POINT * idp;
    int idp_flags;
    int idp_reasons;
    ASN1_INTEGER * crl_number;
    ASN1_INTEGER * base_crl_number;
    uchar sha1_hash[20];
    struct stack_st_GENERAL_NAMES * issuers;
    X509_CRL_METHOD * meth;
    void * meth_data;
};

struct X509_VERIFY_PARAM_st {
    char * name;
    time_t check_time;
    ulong inh_flags;
    ulong flags;
    int purpose;
    int trust;
    int depth;
    struct stack_st_ASN1_OBJECT * policies;
};

struct ssl_st {
    int version;
    int type;
    SSL_METHOD * method;
    BIO * rbio;
    BIO * wbio;
    BIO * bbio;
    int rwstate;
    int in_handshake;
    int (* handshake_func)(SSL *);
    int server;
    int new_session;
    int quiet_shutdown;
    int shutdown;
    int state;
    int rstate;
    BUF_MEM * init_buf;
    void * init_msg;
    int init_num;
    int init_off;
    uchar * packet;
    uint packet_length;
    struct ssl2_state_st * s2;
    struct ssl3_state_st * s3;
    struct dtls1_state_st * d1;
    int read_ahead;
    void (* msg_callback)(int, int, int, void *, size_t, SSL *, void *);
    void * msg_callback_arg;
    int hit;
    X509_VERIFY_PARAM * param;
    struct stack_st_SSL_CIPHER * cipher_list;
    struct stack_st_SSL_CIPHER * cipher_list_by_id;
    int mac_flags;
    EVP_CIPHER_CTX * enc_read_ctx;
    EVP_MD_CTX * read_hash;
    COMP_CTX * expand;
    EVP_CIPHER_CTX * enc_write_ctx;
    EVP_MD_CTX * write_hash;
    COMP_CTX * compress;
    struct cert_st * cert;
    uint sid_ctx_length;
    uchar sid_ctx[32];
    SSL_SESSION * session;
    GEN_SESSION_CB generate_session_id;
    int verify_mode;
    int (* verify_callback)(int, X509_STORE_CTX *);
    void (* info_callback)(SSL *, int, int);
    int error;
    int error_code;
    KSSL_CTX * kssl_ctx;
    uint (* psk_client_callback)(SSL *, char *, char *, uint, uchar *, uint);
    uint (* psk_server_callback)(SSL *, char *, uchar *, uint);
    SSL_CTX * ctx;
    int debug;
    long verify_result;
    CRYPTO_EX_DATA ex_data;
    struct stack_st_X509_NAME * client_CA;
    int references;
    ulong options;
    ulong mode;
    long max_cert_list;
    int first_packet;
    int client_version;
    uint max_send_fragment;
    void (* tlsext_debug_cb)(SSL *, int, int, uchar *, int, void *);
    void * tlsext_debug_arg;
    char * tlsext_hostname;
    int servername_done;
    int tlsext_status_type;
    int tlsext_status_expected;
    struct stack_st_OCSP_RESPID * tlsext_ocsp_ids;
    X509_EXTENSIONS * tlsext_ocsp_exts;
    uchar * tlsext_ocsp_resp;
    int tlsext_ocsp_resplen;
    int tlsext_ticket_expected;
    size_t tlsext_ecpointformatlist_length;
    uchar * tlsext_ecpointformatlist;
    size_t tlsext_ellipticcurvelist_length;
    uchar * tlsext_ellipticcurvelist;
    void * tlsext_opaque_prf_input;
    size_t tlsext_opaque_prf_input_len;
    TLS_SESSION_TICKET_EXT * tlsext_session_ticket;
    tls_session_ticket_ext_cb_fn tls_session_ticket_ext_cb;
    void * tls_session_ticket_ext_cb_arg;
    tls_session_secret_cb_fn tls_session_secret_cb;
    void * tls_session_secret_cb_arg;
    SSL_CTX * initial_ctx;
    uchar * next_proto_negotiated;
    uchar next_proto_negotiated_len;
    struct stack_st_SRTP_PROTECTION_PROFILE * srtp_profiles;
    SRTP_PROTECTION_PROFILE * srtp_profile;
    uint tlsext_heartbeat;
    uint tlsext_hb_pending;
    uint tlsext_hb_seq;
    int renegotiate;
};

union _union_856 {
    GENERAL_NAMES * fullname;
    struct stack_st_X509_NAME_ENTRY * relativename;
};

struct x509_store_st {
    int cache;
    struct stack_st_X509_OBJECT * objs;
    struct stack_st_X509_LOOKUP * get_cert_methods;
    X509_VERIFY_PARAM * param;
    int (* verify)(X509_STORE_CTX *);
    int (* verify_cb)(int, X509_STORE_CTX *);
    int (* get_issuer)(X509 * *, X509_STORE_CTX *, X509 *);
    int (* check_issued)(X509_STORE_CTX *, X509 *, X509 *);
    int (* check_revocation)(X509_STORE_CTX *);
    int (* get_crl)(X509_STORE_CTX *, X509_CRL * *, X509 *);
    int (* check_crl)(X509_STORE_CTX *, X509_CRL *);
    int (* cert_crl)(X509_STORE_CTX *, X509_CRL *, X509 *);
    stack_st_X509 * (* lookup_certs)(X509_STORE_CTX *, X509_NAME *);
    stack_st_X509_CRL * (* lookup_crls)(X509_STORE_CTX *, X509_NAME *);
    int (* cleanup)(X509_STORE_CTX *);
    CRYPTO_EX_DATA ex_data;
    int references;
};

struct dtls1_timeout_st {
    uint read_timeouts;
    uint write_timeouts;
    uint num_alerts;
};

struct stack_st_X509_CRL {
    _STACK stack;
};

struct x509_store_ctx_st {
    X509_STORE * ctx;
    int current_method;
    X509 * cert;
    struct stack_st_X509 * untrusted;
    struct stack_st_X509_CRL * crls;
    X509_VERIFY_PARAM * param;
    void * other_ctx;
    int (* verify)(X509_STORE_CTX *);
    int (* verify_cb)(int, X509_STORE_CTX *);
    int (* get_issuer)(X509 * *, X509_STORE_CTX *, X509 *);
    int (* check_issued)(X509_STORE_CTX *, X509 *, X509 *);
    int (* check_revocation)(X509_STORE_CTX *);
    int (* get_crl)(X509_STORE_CTX *, X509_CRL * *, X509 *);
    int (* check_crl)(X509_STORE_CTX *, X509_CRL *);
    int (* cert_crl)(X509_STORE_CTX *, X509_CRL *, X509 *);
    int (* check_policy)(X509_STORE_CTX *);
    stack_st_X509 * (* lookup_certs)(X509_STORE_CTX *, X509_NAME *);
    stack_st_X509_CRL * (* lookup_crls)(X509_STORE_CTX *, X509_NAME *);
    int (* cleanup)(X509_STORE_CTX *);
    int valid;
    int last_untrusted;
    struct stack_st_X509 * chain;
    X509_POLICY_TREE * tree;
    int explicit_policy;
    int error_depth;
    int error;
    X509 * current_cert;
    X509 * current_issuer;
    X509_CRL * current_crl;
    int current_crl_score;
    uint current_reasons;
    X509_STORE_CTX * parent;
    CRYPTO_EX_DATA ex_data;
};

struct _struct_615 {
    int sess_connect;
    int sess_connect_renegotiate;
    int sess_connect_good;
    int sess_accept;
    int sess_accept_renegotiate;
    int sess_accept_good;
    int sess_miss;
    int sess_timeout;
    int sess_cache_full;
    int sess_hit;
    int sess_cb_hit;
};

struct ssl_ctx_st {
    SSL_METHOD * method;
    struct stack_st_SSL_CIPHER * cipher_list;
    struct stack_st_SSL_CIPHER * cipher_list_by_id;
    struct x509_store_st * cert_store;
    struct lhash_st_SSL_SESSION * sessions;
    ulong session_cache_size;
    struct ssl_session_st * session_cache_head;
    struct ssl_session_st * session_cache_tail;
    int session_cache_mode;
    long session_timeout;
    int (* new_session_cb)(struct ssl_st *, SSL_SESSION *);
    void (* remove_session_cb)(struct ssl_ctx_st *, SSL_SESSION *);
    SSL_SESSION * (* get_session_cb)(struct ssl_st *, uchar *, int, int *);
    struct _struct_615 stats;
    int references;
    int (* app_verify_callback)(X509_STORE_CTX *, void *);
    void * app_verify_arg;
    pem_password_cb * default_passwd_callback;
    void * default_passwd_callback_userdata;
    int (* client_cert_cb)(SSL *, X509 * *, EVP_PKEY * *);
    int (* app_gen_cookie_cb)(SSL *, uchar *, uint *);
    int (* app_verify_cookie_cb)(SSL *, uchar *, uint);
    CRYPTO_EX_DATA ex_data;
    EVP_MD * rsa_md5;
    EVP_MD * md5;
    EVP_MD * sha1;
    struct stack_st_X509 * extra_certs;
    struct stack_st_SSL_COMP * comp_methods;
    void (* info_callback)(SSL *, int, int);
    struct stack_st_X509_NAME * client_CA;
    ulong options;
    ulong mode;
    long max_cert_list;
    struct cert_st * cert;
    int read_ahead;
    void (* msg_callback)(int, int, int, void *, size_t, SSL *, void *);
    void * msg_callback_arg;
    int verify_mode;
    uint sid_ctx_length;
    uchar sid_ctx[32];
    int (* default_verify_callback)(int, X509_STORE_CTX *);
    GEN_SESSION_CB generate_session_id;
    X509_VERIFY_PARAM * param;
    int quiet_shutdown;
    uint max_send_fragment;
    ENGINE * client_cert_engine;
    int (* tlsext_servername_callback)(SSL *, int *, void *);
    void * tlsext_servername_arg;
    uchar tlsext_tick_key_name[16];
    uchar tlsext_tick_hmac_key[16];
    uchar tlsext_tick_aes_key[16];
    int (* tlsext_ticket_key_cb)(SSL *, uchar *, uchar *, EVP_CIPHER_CTX *, HMAC_CTX *, int);
    int (* tlsext_status_cb)(SSL *, void *);
    void * tlsext_status_arg;
    int (* tlsext_opaque_prf_input_callback)(SSL *, void *, size_t, void *);
    void * tlsext_opaque_prf_input_callback_arg;
    char * psk_identity_hint;
    uint (* psk_client_callback)(SSL *, char *, char *, uint, uchar *, uint);
    uint (* psk_server_callback)(SSL *, char *, uchar *, uint);
    uint freelist_max_len;
    struct ssl3_buf_freelist_st * wbuf_freelist;
    struct ssl3_buf_freelist_st * rbuf_freelist;
    int (* next_protos_advertised_cb)(SSL *, uchar * *, uint *, void *);
    void * next_protos_advertised_cb_arg;
    int (* next_proto_select_cb)(SSL *, uchar * *, uchar *, uchar *, uint, void *);
    void * next_proto_select_cb_arg;
    struct stack_st_SRTP_PROTECTION_PROFILE * srtp_profiles;
};

struct _pqueue {
};

struct dtls1_bitmap_st {
    ulong map;
    uchar max_seq_num[8];
};

struct dtls1_state_st {
    uint send_cookie;
    uchar cookie[256];
    uchar rcvd_cookie[256];
    uint cookie_len;
    ushort r_epoch;
    ushort w_epoch;
    DTLS1_BITMAP bitmap;
    DTLS1_BITMAP next_bitmap;
    ushort handshake_write_seq;
    ushort next_handshake_write_seq;
    ushort handshake_read_seq;
    uchar last_write_sequence[8];
    record_pqueue unprocessed_rcds;
    record_pqueue processed_rcds;
    pqueue buffered_messages;
    pqueue sent_messages;
    record_pqueue buffered_app_data;
    uint mtu;
    struct hm_header_st w_msg_hdr;
    struct hm_header_st r_msg_hdr;
    struct dtls1_timeout_st timeout;
    struct timeval next_timeout;
    ushort timeout_duration;
    uchar alert_fragment[2];
    uint alert_fragment_len;
    uchar handshake_fragment[12];
    uint handshake_fragment_len;
    uint retransmitting;
    uint change_cipher_spec_ok;
    uint listen;
};

struct stack_st_X509_OBJECT {
    _STACK stack;
};

struct stack_st_X509 {
    _STACK stack;
};

struct X509_crl_info_st {
    ASN1_INTEGER * version;
    X509_ALGOR * sig_alg;
    X509_NAME * issuer;
    ASN1_TIME * lastUpdate;
    ASN1_TIME * nextUpdate;
    struct stack_st_X509_REVOKED * revoked;
    struct stack_st_X509_EXTENSION * extensions;
    ASN1_ENCODING enc;
};

struct stack_st_X509_REVOKED {
    _STACK stack;
};

struct stack_st_GENERAL_NAMES {
    _STACK stack;
};

struct stack_st_SSL_COMP {
    _STACK stack;
};

struct stack_st_X509_LOOKUP {
    _STACK stack;
};

struct ssl_method_st {
    int version;
    int (* ssl_new)(SSL *);
    void (* ssl_clear)(SSL *);
    void (* ssl_free)(SSL *);
    int (* ssl_accept)(SSL *);
    int (* ssl_connect)(SSL *);
    int (* ssl_read)(SSL *, void *, int);
    int (* ssl_peek)(SSL *, void *, int);
    int (* ssl_write)(SSL *, void *, int);
    int (* ssl_shutdown)(SSL *);
    int (* ssl_renegotiate)(SSL *);
    int (* ssl_renegotiate_check)(SSL *);
    long (* ssl_get_message)(SSL *, int, int, int, long, int *);
    int (* ssl_read_bytes)(SSL *, int, uchar *, int, int);
    int (* ssl_write_bytes)(SSL *, int, void *, int);
    int (* ssl_dispatch_alert)(SSL *);
    long (* ssl_ctrl)(SSL *, int, long, void *);
    long (* ssl_ctx_ctrl)(SSL_CTX *, int, long, void *);
    SSL_CIPHER * (* get_cipher_by_char)(uchar *);
    int (* put_cipher_by_char)(SSL_CIPHER *, uchar *);
    int (* ssl_pending)(SSL *);
    int (* num_ciphers)(void);
    SSL_CIPHER * (* get_cipher)(uint);
    ssl_method_st * (* get_ssl_method)(int);
    long (* get_timeout)(void);
    struct ssl3_enc_method * ssl3_enc;
    int (* ssl_version)(void);
    long (* ssl_callback_ctrl)(SSL *, int, void (* )(void));
    long (* ssl_ctx_callback_ctrl)(SSL_CTX *, int, void (* )(void));
};

struct DIST_POINT_NAME_st {
    int type;
    union _union_856 name;
    X509_NAME * dpname;
};

struct kssl_ctx_st {
    char * service_name;
    char * service_host;
    char * client_princ;
    char * keytab_file;
    char * cred_cache;
    krb5_enctype enctype;
    int length;
    krb5_octet * key;
};

struct X509_POLICY_TREE_st {
};

typedef struct dso_st dso_st, *Pdso_st;

typedef struct dso_st DSO;

typedef struct dso_meth_st dso_meth_st, *Pdso_meth_st;

typedef void (* DSO_FUNC_TYPE)(void);

typedef struct dso_meth_st DSO_METHOD;

typedef char * (* DSO_NAME_CONVERTER_FUNC)(DSO *, char *);

typedef char * (* DSO_MERGER_FUNC)(DSO *, char *, char *);

struct dso_st {
    DSO_METHOD * meth;
    struct stack_st_void * meth_data;
    int references;
    int flags;
    CRYPTO_EX_DATA ex_data;
    DSO_NAME_CONVERTER_FUNC name_converter;
    DSO_MERGER_FUNC merger;
    char * filename;
    char * loaded_filename;
};

struct dso_meth_st {
    char * name;
    int (* dso_load)(DSO *);
    int (* dso_unload)(DSO *);
    void * (* dso_bind_var)(DSO *, char *);
    DSO_FUNC_TYPE (* dso_bind_func)(DSO *, char *);
    long (* dso_ctrl)(DSO *, int, long, void *);
    DSO_NAME_CONVERTER_FUNC dso_name_converter;
    DSO_MERGER_FUNC dso_merger;
    int (* init)(DSO *);
    int (* finish)(DSO *);
    int (* pathbyaddr)(void *, char *, int);
    void * (* globallookup)(char *);
};

typedef struct crypto_threadid_st crypto_threadid_st, *Pcrypto_threadid_st;

struct crypto_threadid_st {
    void * ptr;
    ulong val;
};

typedef struct crypto_threadid_st CRYPTO_THREADID;

typedef struct aes_key_st aes_key_st, *Paes_key_st;

struct aes_key_st {
    uint rd_key[60];
    int rounds;
};

typedef struct aes_key_st AES_KEY;

typedef int (asn1_ps_func)(BIO *, uchar * *, int *, void *);

typedef struct hostent hostent, *Phostent;

struct hostent {
    char * h_name;
    char * * h_aliases;
    int h_addrtype;
    int h_length;
    char * * h_addr_list;
};

typedef long __ssize_t;

typedef __ssize_t ssize_t;

typedef int __pid_t;

typedef int __key_t;

typedef __key_t key_t;

typedef long __off64_t;

typedef int __clockid_t;

typedef int __int32_t;

typedef uint __useconds_t;

typedef uint __socklen_t;

typedef long __clock_t;

typedef uint pthread_key_t;

typedef union pthread_rwlockattr_t pthread_rwlockattr_t, *Ppthread_rwlockattr_t;

union pthread_rwlockattr_t {
    char __size[8];
    long __align;
};

typedef int pthread_once_t;

typedef union pthread_rwlock_t pthread_rwlock_t, *Ppthread_rwlock_t;

typedef struct _struct_19 _struct_19, *P_struct_19;

struct _struct_19 {
    int __lock;
    uint __nr_readers;
    uint __readers_wakeup;
    uint __writer_wakeup;
    uint __nr_readers_queued;
    uint __nr_writers_queued;
    int __writer;
    int __shared;
    ulong __pad1;
    ulong __pad2;
    uint __flags;
};

union pthread_rwlock_t {
    struct _struct_19 __data;
    char __size[56];
    long __align;
};

typedef ulong pthread_t;

typedef struct __dirstream __dirstream, *P__dirstream;

struct __dirstream {
};

typedef struct __dirstream DIR;

typedef struct dirent dirent, *Pdirent;

struct dirent {
    __ino_t d_ino;
    __off_t d_off;
    ushort d_reclen;
    uchar d_type;
    char d_name[256];
};

typedef struct MD4state_st MD4state_st, *PMD4state_st;

struct MD4state_st {
    uint A;
    uint B;
    uint C;
    uint D;
    uint Nl;
    uint Nh;
    uint data[16];
    uint num;
};

typedef struct MD4state_st MD4_CTX;

typedef struct CMAC_CTX_st CMAC_CTX;

typedef struct stack_st_PKCS7_RECIP_INFO stack_st_PKCS7_RECIP_INFO, *Pstack_st_PKCS7_RECIP_INFO;

struct stack_st_PKCS7_RECIP_INFO {
    _STACK stack;
};

typedef struct pkcs7_encrypted_st pkcs7_encrypted_st, *Ppkcs7_encrypted_st;

typedef struct pkcs7_encrypted_st PKCS7_ENCRYPT;

typedef struct pkcs7_enc_content_st pkcs7_enc_content_st, *Ppkcs7_enc_content_st;

typedef struct pkcs7_enc_content_st PKCS7_ENC_CONTENT;

struct pkcs7_encrypted_st {
    ASN1_INTEGER * version;
    PKCS7_ENC_CONTENT * enc_data;
};

struct pkcs7_enc_content_st {
    ASN1_OBJECT * content_type;
    X509_ALGOR * algorithm;
    ASN1_OCTET_STRING * enc_data;
    EVP_CIPHER * cipher;
};

typedef struct pkcs7_digest_st pkcs7_digest_st, *Ppkcs7_digest_st;

typedef struct pkcs7_st pkcs7_st, *Ppkcs7_st;

typedef union _union_444 _union_444, *P_union_444;

typedef struct pkcs7_signed_st pkcs7_signed_st, *Ppkcs7_signed_st;

typedef struct pkcs7_signed_st PKCS7_SIGNED;

typedef struct pkcs7_enveloped_st pkcs7_enveloped_st, *Ppkcs7_enveloped_st;

typedef struct pkcs7_enveloped_st PKCS7_ENVELOPE;

typedef struct pkcs7_signedandenveloped_st pkcs7_signedandenveloped_st, *Ppkcs7_signedandenveloped_st;

typedef struct pkcs7_signedandenveloped_st PKCS7_SIGN_ENVELOPE;

typedef struct pkcs7_digest_st PKCS7_DIGEST;

typedef struct stack_st_PKCS7_SIGNER_INFO stack_st_PKCS7_SIGNER_INFO, *Pstack_st_PKCS7_SIGNER_INFO;

struct pkcs7_digest_st {
    ASN1_INTEGER * version;
    X509_ALGOR * md;
    struct pkcs7_st * contents;
    ASN1_OCTET_STRING * digest;
};

union _union_444 {
    char * ptr;
    ASN1_OCTET_STRING * data;
    PKCS7_SIGNED * sign;
    PKCS7_ENVELOPE * enveloped;
    PKCS7_SIGN_ENVELOPE * signed_and_enveloped;
    PKCS7_DIGEST * digest;
    PKCS7_ENCRYPT * encrypted;
    ASN1_TYPE * other;
};

struct pkcs7_st {
    uchar * asn1;
    long length;
    int state;
    int detached;
    ASN1_OBJECT * type;
    union _union_444 d;
};

struct pkcs7_enveloped_st {
    ASN1_INTEGER * version;
    struct stack_st_PKCS7_RECIP_INFO * recipientinfo;
    PKCS7_ENC_CONTENT * enc_data;
};

struct pkcs7_signedandenveloped_st {
    ASN1_INTEGER * version;
    struct stack_st_X509_ALGOR * md_algs;
    struct stack_st_X509 * cert;
    struct stack_st_X509_CRL * crl;
    struct stack_st_PKCS7_SIGNER_INFO * signer_info;
    PKCS7_ENC_CONTENT * enc_data;
    struct stack_st_PKCS7_RECIP_INFO * recipientinfo;
};

struct pkcs7_signed_st {
    ASN1_INTEGER * version;
    struct stack_st_X509_ALGOR * md_algs;
    struct stack_st_X509 * cert;
    struct stack_st_X509_CRL * crl;
    struct stack_st_PKCS7_SIGNER_INFO * signer_info;
    struct pkcs7_st * contents;
};

struct stack_st_PKCS7_SIGNER_INFO {
    _STACK stack;
};

typedef struct stack_st_PKCS7 stack_st_PKCS7, *Pstack_st_PKCS7;

struct stack_st_PKCS7 {
    _STACK stack;
};

typedef struct pkcs7_signer_info_st pkcs7_signer_info_st, *Ppkcs7_signer_info_st;

typedef struct pkcs7_issuer_and_serial_st pkcs7_issuer_and_serial_st, *Ppkcs7_issuer_and_serial_st;

typedef struct pkcs7_issuer_and_serial_st PKCS7_ISSUER_AND_SERIAL;

struct pkcs7_signer_info_st {
    ASN1_INTEGER * version;
    PKCS7_ISSUER_AND_SERIAL * issuer_and_serial;
    X509_ALGOR * digest_alg;
    struct stack_st_X509_ATTRIBUTE * auth_attr;
    X509_ALGOR * digest_enc_alg;
    ASN1_OCTET_STRING * enc_digest;
    struct stack_st_X509_ATTRIBUTE * unauth_attr;
    EVP_PKEY * pkey;
};

struct pkcs7_issuer_and_serial_st {
    X509_NAME * issuer;
    ASN1_INTEGER * serial;
};

typedef struct pkcs7_st PKCS7;

typedef struct pkcs7_signer_info_st PKCS7_SIGNER_INFO;

typedef struct pkcs7_recip_info_st pkcs7_recip_info_st, *Ppkcs7_recip_info_st;

typedef struct pkcs7_recip_info_st PKCS7_RECIP_INFO;

struct pkcs7_recip_info_st {
    ASN1_INTEGER * version;
    PKCS7_ISSUER_AND_SERIAL * issuer_and_serial;
    X509_ALGOR * key_enc_algor;
    ASN1_OCTET_STRING * enc_key;
    X509 * cert;
};

typedef struct PKCS12 PKCS12, *PPKCS12;

typedef struct PKCS12_MAC_DATA PKCS12_MAC_DATA, *PPKCS12_MAC_DATA;

typedef struct X509_sig_st X509_sig_st, *PX509_sig_st;

typedef struct X509_sig_st X509_SIG;

struct X509_sig_st {
    X509_ALGOR * algor;
    ASN1_OCTET_STRING * digest;
};

struct PKCS12 {
    ASN1_INTEGER * version;
    struct PKCS12_MAC_DATA * mac;
    PKCS7 * authsafes;
};

struct PKCS12_MAC_DATA {
    X509_SIG * dinfo;
    ASN1_OCTET_STRING * salt;
    ASN1_INTEGER * iter;
};

typedef struct pkcs12_bag_st pkcs12_bag_st, *Ppkcs12_bag_st;

typedef union _union_988 _union_988, *P_union_988;

union _union_988 {
    ASN1_OCTET_STRING * x509cert;
    ASN1_OCTET_STRING * x509crl;
    ASN1_OCTET_STRING * octet;
    ASN1_IA5STRING * sdsicert;
    ASN1_TYPE * other;
};

struct pkcs12_bag_st {
    ASN1_OBJECT * type;
    union _union_988 value;
};

typedef struct stack_st_PKCS12_SAFEBAG stack_st_PKCS12_SAFEBAG, *Pstack_st_PKCS12_SAFEBAG;

struct stack_st_PKCS12_SAFEBAG {
    _STACK stack;
};

typedef struct pkcs12_bag_st PKCS12_BAGS;

typedef struct PKCS12_SAFEBAG PKCS12_SAFEBAG, *PPKCS12_SAFEBAG;

typedef union _union_981 _union_981, *P_union_981;

typedef struct pkcs8_priv_key_info_st pkcs8_priv_key_info_st, *Ppkcs8_priv_key_info_st;

struct pkcs8_priv_key_info_st {
    int broken;
    ASN1_INTEGER * version;
    X509_ALGOR * pkeyalg;
    ASN1_TYPE * pkey;
    struct stack_st_X509_ATTRIBUTE * attributes;
};

union _union_981 {
    struct pkcs12_bag_st * bag;
    struct pkcs8_priv_key_info_st * keybag;
    X509_SIG * shkeybag;
    struct stack_st_PKCS12_SAFEBAG * safes;
    ASN1_TYPE * other;
};

struct PKCS12_SAFEBAG {
    ASN1_OBJECT * type;
    union _union_981 value;
    struct stack_st_X509_ATTRIBUTE * attrib;
};

typedef union sigval sigval, *Psigval;

typedef union sigval sigval_t;

union sigval {
    int sival_int;
    void * sival_ptr;
};

typedef struct siginfo siginfo, *Psiginfo;

typedef union _union_1438 _union_1438, *P_union_1438;

typedef struct _struct_1439 _struct_1439, *P_struct_1439;

typedef struct _struct_1440 _struct_1440, *P_struct_1440;

typedef struct _struct_1441 _struct_1441, *P_struct_1441;

typedef struct _struct_1442 _struct_1442, *P_struct_1442;

typedef struct _struct_1443 _struct_1443, *P_struct_1443;

typedef struct _struct_1444 _struct_1444, *P_struct_1444;

struct _struct_1441 {
    __pid_t si_pid;
    __uid_t si_uid;
    sigval_t si_sigval;
};

struct _struct_1443 {
    void * si_addr;
};

struct _struct_1439 {
    __pid_t si_pid;
    __uid_t si_uid;
};

struct _struct_1440 {
    int si_tid;
    int si_overrun;
    sigval_t si_sigval;
};

struct _struct_1444 {
    long si_band;
    int si_fd;
};

struct _struct_1442 {
    __pid_t si_pid;
    __uid_t si_uid;
    int si_status;
    __clock_t si_utime;
    __clock_t si_stime;
};

union _union_1438 {
    int _pad[124];
    struct _struct_1439 _kill;
    struct _struct_1440 _timer;
    struct _struct_1441 _rt;
    struct _struct_1442 _sigchld;
    struct _struct_1443 _sigfault;
    struct _struct_1444 _sigpoll;
};

struct siginfo {
    int si_signo;
    int si_errno;
    int si_code;
    union _union_1438 _sifields;
};

typedef struct siginfo siginfo_t;

typedef struct stack_st_CONF_VALUE stack_st_CONF_VALUE, *Pstack_st_CONF_VALUE;

struct stack_st_CONF_VALUE {
    _STACK stack;
};

typedef struct conf_method_st conf_method_st, *Pconf_method_st;

typedef struct conf_st conf_st, *Pconf_st;

typedef struct conf_st CONF;

typedef struct conf_method_st CONF_METHOD;

typedef struct lhash_st_CONF_VALUE lhash_st_CONF_VALUE, *Plhash_st_CONF_VALUE;

struct lhash_st_CONF_VALUE {
    int dummy;
};

struct conf_st {
    CONF_METHOD * meth;
    void * meth_data;
    struct lhash_st_CONF_VALUE * data;
};

struct conf_method_st {
    char * name;
    CONF * (* create)(CONF_METHOD *);
    int (* init)(CONF *);
    int (* destroy)(CONF *);
    int (* destroy_data)(CONF *);
    int (* load_bio)(CONF *, BIO *, long *);
    int (* dump)(CONF *, BIO *);
    int (* is_number)(CONF *, char);
    int (* to_int)(CONF *, char);
    int (* load)(CONF *, char *, long *);
};

typedef struct conf_imodule_st conf_imodule_st, *Pconf_imodule_st;

typedef struct conf_imodule_st CONF_IMODULE;

struct conf_imodule_st {
};

typedef struct CONF_VALUE CONF_VALUE, *PCONF_VALUE;

struct CONF_VALUE {
    char * section;
    char * name;
    char * value;
};

typedef int (conf_init_func)(CONF_IMODULE *, CONF *);

typedef void (conf_finish_func)(CONF_IMODULE *);

typedef struct conf_module_st conf_module_st, *Pconf_module_st;

typedef struct conf_module_st CONF_MODULE;

struct conf_module_st {
};

typedef struct SHAstate_st SHAstate_st, *PSHAstate_st;

typedef struct SHAstate_st SHA_CTX;

struct SHAstate_st {
    uint h0;
    uint h1;
    uint h2;
    uint h3;
    uint h4;
    uint Nl;
    uint Nh;
    uint data[16];
    uint num;
};

typedef struct SHA256state_st SHA256state_st, *PSHA256state_st;

typedef struct SHA256state_st SHA256_CTX;

struct SHA256state_st {
    uint h[8];
    uint Nl;
    uint Nh;
    uint data[16];
    uint num;
    uint md_len;
};

typedef union _union_314 _union_314, *P_union_314;

union _union_314 {
    ulonglong d[16];
    uchar p[128];
};

typedef struct SHA512state_st SHA512state_st, *PSHA512state_st;

typedef struct SHA512state_st SHA512_CTX;

struct SHA512state_st {
    ulonglong h[8];
    ulonglong Nl;
    ulonglong Nh;
    union _union_314 u;
    uint num;
    uint md_len;
};

typedef struct CMS_RevocationInfoChoice_st CMS_RevocationInfoChoice_st, *PCMS_RevocationInfoChoice_st;

typedef struct CMS_RevocationInfoChoice_st CMS_RevocationInfoChoice;

struct CMS_RevocationInfoChoice_st {
};

typedef struct CMS_SignerInfo_st CMS_SignerInfo_st, *PCMS_SignerInfo_st;

typedef struct CMS_SignerInfo_st CMS_SignerInfo;

struct CMS_SignerInfo_st {
};

typedef struct stack_st_CMS_RecipientInfo stack_st_CMS_RecipientInfo, *Pstack_st_CMS_RecipientInfo;

struct stack_st_CMS_RecipientInfo {
};

typedef struct CMS_ReceiptRequest_st CMS_ReceiptRequest_st, *PCMS_ReceiptRequest_st;

typedef struct CMS_ReceiptRequest_st CMS_ReceiptRequest;

struct CMS_ReceiptRequest_st {
};

typedef struct CMS_CertificateChoices CMS_CertificateChoices, *PCMS_CertificateChoices;

struct CMS_CertificateChoices {
};

typedef struct CMS_ContentInfo_st CMS_ContentInfo_st, *PCMS_ContentInfo_st;

struct CMS_ContentInfo_st {
};

typedef struct CMS_ContentInfo_st CMS_ContentInfo;

typedef struct stack_st_CMS_SignerInfo stack_st_CMS_SignerInfo, *Pstack_st_CMS_SignerInfo;

struct stack_st_CMS_SignerInfo {
    _STACK stack;
};

typedef struct CMS_RecipientInfo_st CMS_RecipientInfo_st, *PCMS_RecipientInfo_st;

typedef struct CMS_RecipientInfo_st CMS_RecipientInfo;

struct CMS_RecipientInfo_st {
};

/*
typedef void * __gnuc_va_list;
*/

typedef __gnuc_va_list va_list;

typedef struct stack_st_OPENSSL_PSTRING stack_st_OPENSSL_PSTRING, *Pstack_st_OPENSSL_PSTRING;

struct stack_st_OPENSSL_PSTRING {
    _STACK stack;
};

typedef struct txt_db_st txt_db_st, *Ptxt_db_st;

typedef char * OPENSSL_STRING;

typedef struct txt_db_st TXT_DB;

typedef struct lhash_st_OPENSSL_STRING lhash_st_OPENSSL_STRING, *Plhash_st_OPENSSL_STRING;

struct lhash_st_OPENSSL_STRING {
    int dummy;
};

struct txt_db_st {
    int num_fields;
    struct stack_st_OPENSSL_PSTRING * data;
    struct lhash_st_OPENSSL_STRING * * index;
    int (* qual)(OPENSSL_STRING *);
    long error;
    long arg1;
    long arg2;
    OPENSSL_STRING * arg_row;
};

typedef struct RIPEMD160state_st RIPEMD160state_st, *PRIPEMD160state_st;

typedef struct RIPEMD160state_st RIPEMD160_CTX;

struct RIPEMD160state_st {
    uint A;
    uint B;
    uint C;
    uint D;
    uint E;
    uint Nl;
    uint Nh;
    uint data[16];
    uint num;
};

typedef struct rc4_key_st rc4_key_st, *Prc4_key_st;

typedef struct rc4_key_st RC4_KEY;

struct rc4_key_st {
    uint x;
    uint y;
    uint data[256];
};

typedef struct bf_key_st bf_key_st, *Pbf_key_st;

typedef struct bf_key_st BF_KEY;

struct bf_key_st {
    uint P[18];
    uint S[1024];
};

typedef struct sigaction sigaction, *Psigaction;

typedef union _union_1454 _union_1454, *P_union_1454;

typedef struct __sigset_t __sigset_t, *P__sigset_t;

typedef void (* __sighandler_t)(int);

struct __sigset_t {
    ulong __val[128];
};

union _union_1454 {
    __sighandler_t sa_handler;
    void (* sa_sigaction)(int, siginfo_t *, void *);
};

struct sigaction {
    union _union_1454 __sigaction_handler;
    struct __sigset_t sa_mask;
    int sa_flags;
    void (* sa_restorer)(void);
};

typedef struct rc2_key_st rc2_key_st, *Prc2_key_st;

typedef struct rc2_key_st RC2_KEY;

struct rc2_key_st {
    uint data[64];
};

typedef struct ECDSA_SIG_st ECDSA_SIG_st, *PECDSA_SIG_st;

struct ECDSA_SIG_st {
    BIGNUM * r;
    BIGNUM * s;
};

typedef struct ECDSA_SIG_st ECDSA_SIG;

typedef struct ec_group_st ec_group_st, *Pec_group_st;

typedef struct ec_group_st EC_GROUP;

struct ec_group_st {
};

typedef struct EC_builtin_curve EC_builtin_curve, *PEC_builtin_curve;

struct EC_builtin_curve {
    int nid;
    char * comment;
};

typedef struct ec_method_st ec_method_st, *Pec_method_st;

struct ec_method_st {
};

typedef enum enum_295 {
    POINT_CONVERSION_COMPRESSED=2,
    POINT_CONVERSION_HYBRID=6,
    POINT_CONVERSION_UNCOMPRESSED=4
} enum_295;

typedef struct ec_method_st EC_METHOD;

typedef struct ec_point_st ec_point_st, *Pec_point_st;

typedef struct ec_point_st EC_POINT;

struct ec_point_st {
};

typedef enum enum_295 point_conversion_form_t;

typedef enum UI_string_types {
    UIT_BOOLEAN=3,
    UIT_ERROR=5,
    UIT_INFO=4,
    UIT_NONE=0,
    UIT_PROMPT=1,
    UIT_VERIFY=2
} UI_string_types;

typedef struct ui_string_st ui_string_st, *Pui_string_st;

struct ui_string_st {
};

typedef struct ui_string_st UI_STRING;

typedef struct obj_name_st obj_name_st, *Pobj_name_st;

struct obj_name_st {
    int type;
    int alias;
    char * name;
    char * data;
};

typedef struct obj_name_st OBJ_NAME;

typedef union _union_771 _union_771, *P_union_771;

typedef uchar DES_cblock[8];

union _union_771 {
    DES_cblock cblock;
    uint deslong[2];
};

typedef struct DES_ks DES_ks, *PDES_ks;

typedef struct DES_ks DES_key_schedule;

struct DES_ks {
    union _union_771 ks[16];
};

typedef uchar const_DES_cblock[8];

typedef int (* __compar_fn_t)(void *, void *);

typedef int (* ENGINE_GEN_INT_FUNC_PTR)(ENGINE *);

typedef int (* ENGINE_DIGESTS_PTR)(ENGINE *, EVP_MD * *, int * *, int);

typedef struct ENGINE_CMD_DEFN_st ENGINE_CMD_DEFN_st, *PENGINE_CMD_DEFN_st;

typedef struct ENGINE_CMD_DEFN_st ENGINE_CMD_DEFN;

struct ENGINE_CMD_DEFN_st {
    uint cmd_num;
    char * cmd_name;
    char * cmd_desc;
    uint cmd_flags;
};

typedef struct ui_method_st ui_method_st, *Pui_method_st;

typedef struct ui_method_st UI_METHOD;

typedef int (* ENGINE_SSL_CLIENT_CERT_PTR)(ENGINE *, SSL *, struct stack_st_X509_NAME *, X509 * *, EVP_PKEY * *, struct stack_st_X509 * *, UI_METHOD *, void *);

struct ui_method_st {
};

typedef int (* ENGINE_PKEY_ASN1_METHS_PTR)(ENGINE *, EVP_PKEY_ASN1_METHOD * *, int * *, int);

typedef struct evp_pkey_method_st evp_pkey_method_st, *Pevp_pkey_method_st;

typedef struct evp_pkey_method_st EVP_PKEY_METHOD;

typedef int (* ENGINE_PKEY_METHS_PTR)(ENGINE *, EVP_PKEY_METHOD * *, int * *, int);

struct evp_pkey_method_st {
};

typedef int (* ENGINE_CIPHERS_PTR)(ENGINE *, EVP_CIPHER * *, int * *, int);

typedef EVP_PKEY * (* ENGINE_LOAD_KEY_PTR)(ENGINE *, char *, UI_METHOD *, void *);

typedef int (* ENGINE_CTRL_FUNC_PTR)(ENGINE *, int, long, void *, void (* )(void));

typedef ushort sa_family_t;

typedef void _IO_lock_t;

typedef struct _IO_marker _IO_marker, *P_IO_marker;

typedef struct _IO_FILE _IO_FILE, *P_IO_FILE;

/*
struct _IO_marker {
    struct _IO_marker * _next;
    struct _IO_FILE * _sbuf;
    int _pos;
};
*/
/*
struct _IO_FILE {
    int _flags;
    char * _IO_read_ptr;
    char * _IO_read_end;
    char * _IO_read_base;
    char * _IO_write_base;
    char * _IO_write_ptr;
    char * _IO_write_end;
    char * _IO_buf_base;
    char * _IO_buf_end;
    char * _IO_save_base;
    char * _IO_backup_base;
    char * _IO_save_end;
    struct _IO_marker * _markers;
    struct _IO_FILE * _chain;
    int _fileno;
    int _flags2;
    __off_t _old_offset;
    ushort _cur_column;
    char _vtable_offset;
    char _shortbuf[1];
    _IO_lock_t * _lock;
    __off64_t _offset;
    void * __pad1;
    void * __pad2;
    void * __pad3;
    void * __pad4;
    size_t __pad5;
    int _mode;
    char _unused2[15];
};
*/
typedef struct POLICYQUALINFO_st POLICYQUALINFO_st, *PPOLICYQUALINFO_st;

typedef struct POLICYQUALINFO_st POLICYQUALINFO;

typedef union _union_870 _union_870, *P_union_870;

typedef struct USERNOTICE_st USERNOTICE_st, *PUSERNOTICE_st;

typedef struct USERNOTICE_st USERNOTICE;

typedef struct NOTICEREF_st NOTICEREF_st, *PNOTICEREF_st;

typedef struct NOTICEREF_st NOTICEREF;

typedef struct stack_st_ASN1_INTEGER stack_st_ASN1_INTEGER, *Pstack_st_ASN1_INTEGER;

struct NOTICEREF_st {
    ASN1_STRING * organization;
    struct stack_st_ASN1_INTEGER * noticenos;
};

union _union_870 {
    ASN1_IA5STRING * cpsuri;
    USERNOTICE * usernotice;
    ASN1_TYPE * other;
};

struct POLICYQUALINFO_st {
    ASN1_OBJECT * pqualid;
    union _union_870 d;
};

struct USERNOTICE_st {
    NOTICEREF * noticeref;
    ASN1_STRING * exptext;
};

struct stack_st_ASN1_INTEGER {
    _STACK stack;
};

typedef struct POLICY_CONSTRAINTS_st POLICY_CONSTRAINTS_st, *PPOLICY_CONSTRAINTS_st;

typedef struct POLICY_CONSTRAINTS_st POLICY_CONSTRAINTS;

struct POLICY_CONSTRAINTS_st {
    ASN1_INTEGER * requireExplicitPolicy;
    ASN1_INTEGER * inhibitPolicyMapping;
};

typedef struct GENERAL_SUBTREE_st GENERAL_SUBTREE_st, *PGENERAL_SUBTREE_st;

typedef struct GENERAL_SUBTREE_st GENERAL_SUBTREE;

typedef struct GENERAL_NAME_st GENERAL_NAME_st, *PGENERAL_NAME_st;

typedef struct GENERAL_NAME_st GENERAL_NAME;

typedef union _union_848 _union_848, *P_union_848;

typedef struct otherName_st otherName_st, *PotherName_st;

typedef struct otherName_st OTHERNAME;

typedef struct EDIPartyName_st EDIPartyName_st, *PEDIPartyName_st;

typedef struct EDIPartyName_st EDIPARTYNAME;

union _union_848 {
    char * ptr;
    OTHERNAME * otherName;
    ASN1_IA5STRING * rfc822Name;
    ASN1_IA5STRING * dNSName;
    ASN1_TYPE * x400Address;
    X509_NAME * directoryName;
    EDIPARTYNAME * ediPartyName;
    ASN1_IA5STRING * uniformResourceIdentifier;
    ASN1_OCTET_STRING * iPAddress;
    ASN1_OBJECT * registeredID;
    ASN1_OCTET_STRING * ip;
    X509_NAME * dirn;
    ASN1_IA5STRING * ia5;
    ASN1_OBJECT * rid;
    ASN1_TYPE * other;
};

struct GENERAL_NAME_st {
    int type;
    union _union_848 d;
};

struct GENERAL_SUBTREE_st {
    GENERAL_NAME * base;
    ASN1_INTEGER * minimum;
    ASN1_INTEGER * maximum;
};

struct EDIPartyName_st {
    ASN1_STRING * nameAssigner;
    ASN1_STRING * partyName;
};

struct otherName_st {
    ASN1_OBJECT * type_id;
    ASN1_TYPE * value;
};

typedef struct PROXY_CERT_INFO_EXTENSION_st PROXY_CERT_INFO_EXTENSION_st, *PPROXY_CERT_INFO_EXTENSION_st;

typedef struct PROXY_CERT_INFO_EXTENSION_st PROXY_CERT_INFO_EXTENSION;

typedef struct PROXY_POLICY_st PROXY_POLICY_st, *PPROXY_POLICY_st;

typedef struct PROXY_POLICY_st PROXY_POLICY;

struct PROXY_POLICY_st {
    ASN1_OBJECT * policyLanguage;
    ASN1_OCTET_STRING * policy;
};

struct PROXY_CERT_INFO_EXTENSION_st {
    ASN1_INTEGER * pcPathLengthConstraint;
    PROXY_POLICY * proxyPolicy;
};

typedef struct PKEY_USAGE_PERIOD_st PKEY_USAGE_PERIOD_st, *PPKEY_USAGE_PERIOD_st;

typedef struct PKEY_USAGE_PERIOD_st PKEY_USAGE_PERIOD;

struct PKEY_USAGE_PERIOD_st {
    ASN1_GENERALIZEDTIME * notBefore;
    ASN1_GENERALIZEDTIME * notAfter;
};

typedef struct v3_ext_method v3_ext_method, *Pv3_ext_method;

typedef struct v3_ext_ctx v3_ext_ctx, *Pv3_ext_ctx;

typedef void * (* X509V3_EXT_V2I)(struct v3_ext_method *, struct v3_ext_ctx *, struct stack_st_CONF_VALUE *);

typedef struct ASN1_ITEM_st ASN1_ITEM_st, *PASN1_ITEM_st;

typedef struct ASN1_ITEM_st ASN1_ITEM;

typedef ASN1_ITEM ASN1_ITEM_EXP;

typedef void * (* X509V3_EXT_NEW)(void);

typedef void (* X509V3_EXT_FREE)(void *);

typedef void * (* X509V3_EXT_D2I)(void *, uchar * *, long);

typedef int (* X509V3_EXT_I2D)(void *, uchar * *);

typedef char * (* X509V3_EXT_I2S)(struct v3_ext_method *, void *);

typedef void * (* X509V3_EXT_S2I)(struct v3_ext_method *, struct v3_ext_ctx *, char *);

typedef stack_st_CONF_VALUE * (* X509V3_EXT_I2V)(struct v3_ext_method *, void *, struct stack_st_CONF_VALUE *);

typedef int (* X509V3_EXT_I2R)(struct v3_ext_method *, void *, BIO *, int);

typedef void * (* X509V3_EXT_R2I)(struct v3_ext_method *, struct v3_ext_ctx *, char *);

typedef struct X509_req_st X509_req_st, *PX509_req_st;

typedef struct X509_req_st X509_REQ;

typedef struct X509V3_CONF_METHOD_st X509V3_CONF_METHOD_st, *PX509V3_CONF_METHOD_st;

typedef struct X509V3_CONF_METHOD_st X509V3_CONF_METHOD;

typedef struct ASN1_TEMPLATE_st ASN1_TEMPLATE_st, *PASN1_TEMPLATE_st;

typedef struct ASN1_TEMPLATE_st ASN1_TEMPLATE;

typedef struct X509_req_info_st X509_req_info_st, *PX509_req_info_st;

typedef struct X509_req_info_st X509_REQ_INFO;

struct X509_req_info_st {
    ASN1_ENCODING enc;
    ASN1_INTEGER * version;
    X509_NAME * subject;
    X509_PUBKEY * pubkey;
    struct stack_st_X509_ATTRIBUTE * attributes;
};

struct ASN1_ITEM_st {
    char itype;
    long utype;
    ASN1_TEMPLATE * templates;
    long tcount;
    void * funcs;
    long size;
    char * sname;
};

struct v3_ext_method {
    int ext_nid;
    int ext_flags;
    ASN1_ITEM_EXP * it;
    X509V3_EXT_NEW ext_new;
    X509V3_EXT_FREE ext_free;
    X509V3_EXT_D2I d2i;
    X509V3_EXT_I2D i2d;
    X509V3_EXT_I2S i2s;
    X509V3_EXT_S2I s2i;
    X509V3_EXT_I2V i2v;
    X509V3_EXT_V2I v2i;
    X509V3_EXT_I2R i2r;
    X509V3_EXT_R2I r2i;
    void * usr_data;
};

struct X509V3_CONF_METHOD_st {
    char * (* get_string)(void *, char *, char *);
    stack_st_CONF_VALUE * (* get_section)(void *, char *);
    void (* free_string)(void *, char *);
    void (* free_section)(void *, struct stack_st_CONF_VALUE *);
};

struct ASN1_TEMPLATE_st {
    ulong flags;
    long tag;
    ulong offset;
    char * field_name;
    ASN1_ITEM_EXP * item;
};

struct X509_req_st {
    X509_REQ_INFO * req_info;
    X509_ALGOR * sig_alg;
    ASN1_BIT_STRING * signature;
    int references;
};

struct v3_ext_ctx {
    int flags;
    X509 * issuer_cert;
    X509 * subject_cert;
    X509_REQ * subject_req;
    X509_CRL * crl;
    X509V3_CONF_METHOD * db_meth;
    void * db;
};

typedef struct POLICYINFO_st POLICYINFO_st, *PPOLICYINFO_st;

typedef struct POLICYINFO_st POLICYINFO;

typedef struct stack_st_POLICYQUALINFO stack_st_POLICYQUALINFO, *Pstack_st_POLICYQUALINFO;

struct POLICYINFO_st {
    ASN1_OBJECT * policyid;
    struct stack_st_POLICYQUALINFO * qualifiers;
};

struct stack_st_POLICYQUALINFO {
    _STACK stack;
};

typedef union _union_926 _union_926, *P_union_926;

typedef struct ASRange_st ASRange_st, *PASRange_st;

typedef struct ASRange_st ASRange;

union _union_926 {
    ASN1_INTEGER * id;
    ASRange * range;
};

struct ASRange_st {
    ASN1_INTEGER * min;
    ASN1_INTEGER * * max;
};

typedef struct IPAddressRange_st IPAddressRange_st, *PIPAddressRange_st;

struct IPAddressRange_st {
    ASN1_BIT_STRING * min;
    ASN1_BIT_STRING * * max;
};

typedef struct stack_st_IPAddressOrRange stack_st_IPAddressOrRange, *Pstack_st_IPAddressOrRange;

typedef struct stack_st_IPAddressOrRange IPAddressOrRanges;

struct stack_st_IPAddressOrRange {
    _STACK stack;
};

typedef struct ASIdentifiers_st ASIdentifiers;

typedef struct SXNET_ID_st SXNET_ID_st, *PSXNET_ID_st;

typedef struct SXNET_ID_st SXNETID;

struct SXNET_ID_st {
    ASN1_INTEGER * zone;
    ASN1_OCTET_STRING * user;
};

typedef struct ACCESS_DESCRIPTION_st ACCESS_DESCRIPTION_st, *PACCESS_DESCRIPTION_st;

typedef struct ACCESS_DESCRIPTION_st ACCESS_DESCRIPTION;

struct ACCESS_DESCRIPTION_st {
    ASN1_OBJECT * method;
    GENERAL_NAME * location;
};

typedef struct BASIC_CONSTRAINTS_st BASIC_CONSTRAINTS_st, *PBASIC_CONSTRAINTS_st;

typedef struct BASIC_CONSTRAINTS_st BASIC_CONSTRAINTS;

struct BASIC_CONSTRAINTS_st {
    int ca;
    ASN1_INTEGER * pathlen;
};

typedef struct IPAddressChoice_st IPAddressChoice_st, *PIPAddressChoice_st;

typedef struct IPAddressChoice_st IPAddressChoice;

typedef union _union_938 _union_938, *P_union_938;

union _union_938 {
    ASN1_NULL * inherit;
    IPAddressOrRanges * addressesOrRanges;
};

struct IPAddressChoice_st {
    int type;
    union _union_938 u;
};

typedef union _union_934 _union_934, *P_union_934;

typedef struct IPAddressRange_st IPAddressRange;

union _union_934 {
    ASN1_BIT_STRING * addressPrefix;
    IPAddressRange * addressRange;
};

typedef struct IPAddressFamily_st IPAddressFamily_st, *PIPAddressFamily_st;

typedef struct IPAddressFamily_st IPAddressFamily;

struct IPAddressFamily_st {
    ASN1_OCTET_STRING * addressFamily;
    IPAddressChoice * ipAddressChoice;
};

typedef struct SXNET_st SXNET_st, *PSXNET_st;

typedef struct SXNET_st SXNET;

typedef struct stack_st_SXNETID stack_st_SXNETID, *Pstack_st_SXNETID;

struct SXNET_st {
    ASN1_INTEGER * version;
    struct stack_st_SXNETID * ids;
};

struct stack_st_SXNETID {
    _STACK stack;
};

typedef struct stack_st_ASN1_OBJECT EXTENDED_KEY_USAGE;

typedef struct POLICY_MAPPING_st POLICY_MAPPING_st, *PPOLICY_MAPPING_st;

typedef struct POLICY_MAPPING_st POLICY_MAPPING;

struct POLICY_MAPPING_st {
    ASN1_OBJECT * issuerDomainPolicy;
    ASN1_OBJECT * subjectDomainPolicy;
};

typedef struct stack_st_POLICYINFO stack_st_POLICYINFO, *Pstack_st_POLICYINFO;

typedef struct stack_st_POLICYINFO CERTIFICATEPOLICIES;

struct stack_st_POLICYINFO {
    _STACK stack;
};

typedef struct IPAddressOrRange_st IPAddressOrRange_st, *PIPAddressOrRange_st;

struct IPAddressOrRange_st {
    int type;
    union _union_934 u;
};

typedef struct stack_st_DIST_POINT CRL_DIST_POINTS;

typedef struct x509_purpose_st x509_purpose_st, *Px509_purpose_st;

struct x509_purpose_st {
    int purpose;
    int trust;
    int flags;
    int (* check_purpose)(struct x509_purpose_st *, X509 *, int);
    char * name;
    char * sname;
    void * usr_data;
};

typedef struct stack_st_ACCESS_DESCRIPTION stack_st_ACCESS_DESCRIPTION, *Pstack_st_ACCESS_DESCRIPTION;

typedef struct stack_st_ACCESS_DESCRIPTION AUTHORITY_INFO_ACCESS;

struct stack_st_ACCESS_DESCRIPTION {
    _STACK stack;
};

typedef struct IPAddressOrRange_st IPAddressOrRange;

typedef struct ASIdOrRange_st ASIdOrRange_st, *PASIdOrRange_st;

typedef struct ASIdOrRange_st ASIdOrRange;

struct ASIdOrRange_st {
    int type;
    union _union_926 u;
};

typedef struct v3_ext_method X509V3_EXT_METHOD;

typedef struct x509_purpose_st X509_PURPOSE;

typedef struct rsa_pss_params_st rsa_pss_params_st, *Prsa_pss_params_st;

struct rsa_pss_params_st {
    X509_ALGOR * hashAlgorithm;
    X509_ALGOR * maskGenAlgorithm;
    ASN1_INTEGER * saltLength;
    ASN1_INTEGER * trailerField;
};

typedef struct rsa_pss_params_st RSA_PSS_PARAMS;

typedef struct PBKDF2PARAM_st PBKDF2PARAM_st, *PPBKDF2PARAM_st;

typedef struct PBKDF2PARAM_st PBKDF2PARAM;

struct PBKDF2PARAM_st {
    ASN1_TYPE * salt;
    ASN1_INTEGER * iter;
    ASN1_INTEGER * keylength;
    X509_ALGOR * prf;
};

typedef struct Netscape_spkac_st Netscape_spkac_st, *PNetscape_spkac_st;

struct Netscape_spkac_st {
    X509_PUBKEY * pubkey;
    ASN1_IA5STRING * challenge;
};

typedef struct X509_info_st X509_info_st, *PX509_info_st;

typedef struct private_key_st private_key_st, *Pprivate_key_st;

typedef struct private_key_st X509_PKEY;

typedef struct evp_cipher_info_st evp_cipher_info_st, *Pevp_cipher_info_st;

typedef struct evp_cipher_info_st EVP_CIPHER_INFO;

struct evp_cipher_info_st {
    EVP_CIPHER * cipher;
    uchar iv[16];
};

struct X509_info_st {
    X509 * x509;
    X509_CRL * crl;
    X509_PKEY * x_pkey;
    EVP_CIPHER_INFO enc_cipher;
    int enc_len;
    char * enc_data;
    int references;
};

struct private_key_st {
    int version;
    X509_ALGOR * enc_algor;
    ASN1_OCTET_STRING * enc_pkey;
    EVP_PKEY * dec_pkey;
    int key_length;
    char * key_data;
    int key_free;
    EVP_CIPHER_INFO cipher;
    int references;
};

typedef struct PBE2PARAM_st PBE2PARAM_st, *PPBE2PARAM_st;

typedef struct PBE2PARAM_st PBE2PARAM;

struct PBE2PARAM_st {
    X509_ALGOR * keyfunc;
    X509_ALGOR * encryption;
};

typedef struct Netscape_spki_st Netscape_spki_st, *PNetscape_spki_st;

typedef struct Netscape_spki_st NETSCAPE_SPKI;

typedef struct Netscape_spkac_st NETSCAPE_SPKAC;

struct Netscape_spki_st {
    NETSCAPE_SPKAC * spkac;
    X509_ALGOR * sig_algor;
    ASN1_BIT_STRING * signature;
};

typedef struct x509_attributes_st x509_attributes_st, *Px509_attributes_st;

typedef struct x509_attributes_st X509_ATTRIBUTE;

typedef union _union_330 _union_330, *P_union_330;

typedef struct stack_st_ASN1_TYPE stack_st_ASN1_TYPE, *Pstack_st_ASN1_TYPE;

union _union_330 {
    char * ptr;
    struct stack_st_ASN1_TYPE * set;
    ASN1_TYPE * single;
};

struct x509_attributes_st {
    ASN1_OBJECT * object;
    int single;
    union _union_330 value;
};

struct stack_st_ASN1_TYPE {
    _STACK stack;
};

typedef struct x509_trust_st x509_trust_st, *Px509_trust_st;

struct x509_trust_st {
    int trust;
    int flags;
    int (* check_trust)(struct x509_trust_st *, X509 *, int);
    char * name;
    int arg1;
    void * arg2;
};

typedef struct stack_st_X509_INFO stack_st_X509_INFO, *Pstack_st_X509_INFO;

struct stack_st_X509_INFO {
    _STACK stack;
};

typedef struct X509_name_entry_st X509_name_entry_st, *PX509_name_entry_st;

typedef struct X509_name_entry_st X509_NAME_ENTRY;

struct X509_name_entry_st {
    ASN1_OBJECT * object;
    ASN1_STRING * value;
    int set;
    int size;
};

typedef struct PBEPARAM_st PBEPARAM_st, *PPBEPARAM_st;

typedef struct PBEPARAM_st PBEPARAM;

struct PBEPARAM_st {
    ASN1_OCTET_STRING * salt;
    ASN1_INTEGER * iter;
};

typedef struct Netscape_certificate_sequence Netscape_certificate_sequence, *PNetscape_certificate_sequence;

typedef struct Netscape_certificate_sequence NETSCAPE_CERT_SEQUENCE;

struct Netscape_certificate_sequence {
    ASN1_OBJECT * type;
    struct stack_st_X509 * certs;
};

typedef struct X509_info_st X509_INFO;

typedef struct X509_extension_st X509_extension_st, *PX509_extension_st;

typedef struct X509_extension_st X509_EXTENSION;

struct X509_extension_st {
    ASN1_OBJECT * object;
    ASN1_BOOLEAN critical;
    ASN1_OCTET_STRING * value;
};

typedef struct x509_trust_st X509_TRUST;

typedef struct stack_st_X509_ALGOR X509_ALGORS;

typedef struct addrinfo addrinfo, *Paddrinfo;

typedef __socklen_t socklen_t;

typedef struct sockaddr sockaddr, *Psockaddr;

struct addrinfo {
    int ai_flags;
    int ai_family;
    int ai_socktype;
    int ai_protocol;
    socklen_t ai_addrlen;
    struct sockaddr * ai_addr;
    char * ai_canonname;
    struct addrinfo * ai_next;
};

struct sockaddr {
    sa_family_t sa_family;
    char sa_data[14];
};

typedef struct seed_key_st seed_key_st, *Pseed_key_st;

typedef struct seed_key_st SEED_KEY_SCHEDULE;

struct seed_key_st {
    uint data[32];
};

typedef int (* LHASH_COMP_FN_TYPE)(void *, void *);

typedef ulong (* LHASH_HASH_FN_TYPE)(void *);

typedef struct _IO_FILE FILE;

typedef struct stack_st_X509_POLICY_NODE stack_st_X509_POLICY_NODE, *Pstack_st_X509_POLICY_NODE;

struct stack_st_X509_POLICY_NODE {
    _STACK stack;
};

typedef struct x509_object_st x509_object_st, *Px509_object_st;

typedef union _union_381 _union_381, *P_union_381;

union _union_381 {
    char * ptr;
    X509 * x509;
    X509_CRL * crl;
    EVP_PKEY * pkey;
};

struct x509_object_st {
    int type;
    union _union_381 data;
};

typedef struct x509_lookup_method_st x509_lookup_method_st, *Px509_lookup_method_st;

typedef struct x509_lookup_st x509_lookup_st, *Px509_lookup_st;

typedef struct x509_lookup_st X509_LOOKUP;

typedef struct x509_object_st X509_OBJECT;

typedef struct x509_lookup_method_st X509_LOOKUP_METHOD;

struct x509_lookup_method_st {
    char * name;
    int (* new_item)(X509_LOOKUP *);
    void (* free)(X509_LOOKUP *);
    int (* init)(X509_LOOKUP *);
    int (* shutdown)(X509_LOOKUP *);
    int (* ctrl)(X509_LOOKUP *, int, char *, long, char * *);
    int (* get_by_subject)(X509_LOOKUP *, int, X509_NAME *, X509_OBJECT *);
    int (* get_by_issuer_serial)(X509_LOOKUP *, int, X509_NAME *, ASN1_INTEGER *, X509_OBJECT *);
    int (* get_by_fingerprint)(X509_LOOKUP *, int, uchar *, int, X509_OBJECT *);
    int (* get_by_alias)(X509_LOOKUP *, int, char *, int, X509_OBJECT *);
};

struct x509_lookup_st {
    int init;
    int skip;
    X509_LOOKUP_METHOD * method;
    char * method_data;
    X509_STORE * store_ctx;
};

typedef struct pkcs8_priv_key_info_st PKCS8_PRIV_KEY_INFO;

typedef struct ocsp_response_st ocsp_response_st, *Pocsp_response_st;

typedef struct ocsp_resp_bytes_st ocsp_resp_bytes_st, *Pocsp_resp_bytes_st;

typedef struct ocsp_resp_bytes_st OCSP_RESPBYTES;

struct ocsp_resp_bytes_st {
    ASN1_OBJECT * responseType;
    ASN1_OCTET_STRING * response;
};

struct ocsp_response_st {
    ASN1_ENUMERATED * responseStatus;
    OCSP_RESPBYTES * responseBytes;
};

typedef int (CRYPTO_EX_new)(void *, void *, CRYPTO_EX_DATA *, int, long, void *);

typedef struct ocsp_response_st OCSP_RESPONSE;

typedef struct ocsp_responder_id_st ocsp_responder_id_st, *Pocsp_responder_id_st;

typedef struct ocsp_responder_id_st OCSP_RESPID;

typedef union _union_958 _union_958, *P_union_958;

union _union_958 {
    X509_NAME * byName;
    ASN1_OCTET_STRING * byKey;
};

struct ocsp_responder_id_st {
    int type;
    union _union_958 value;
};

typedef struct v3_ext_ctx X509V3_CTX;

typedef struct ocsp_req_ctx_st ocsp_req_ctx_st, *Pocsp_req_ctx_st;

typedef struct ocsp_req_ctx_st OCSP_REQ_CTX;

struct ocsp_req_ctx_st {
};

typedef struct x509_revoked_st x509_revoked_st, *Px509_revoked_st;

typedef struct x509_revoked_st X509_REVOKED;

struct x509_revoked_st {
    ASN1_INTEGER * serialNumber;
    ASN1_TIME * revocationDate;
    struct stack_st_X509_EXTENSION * extensions;
    struct stack_st_GENERAL_NAME * issuer;
    int reason;
    int sequence;
};

typedef void (CRYPTO_EX_free)(void *, void *, CRYPTO_EX_DATA *, int, long, void *);

typedef struct asn1_pctx_st asn1_pctx_st, *Pasn1_pctx_st;

struct asn1_pctx_st {
};

typedef struct bn_recp_ctx_st bn_recp_ctx_st, *Pbn_recp_ctx_st;

typedef struct bn_recp_ctx_st BN_RECP_CTX;

struct bn_recp_ctx_st {
    BIGNUM N;
    BIGNUM Nr;
    int num_bits;
    int shift;
    int flags;
};

typedef struct DIST_POINT_st DIST_POINT_st, *PDIST_POINT_st;

struct DIST_POINT_st {
    DIST_POINT_NAME * distpoint;
    ASN1_BIT_STRING * reasons;
    GENERAL_NAMES * CRLissuer;
    int dp_reasons;
};

typedef struct ui_st ui_st, *Pui_st;

typedef struct ui_st UI;

struct ui_st {
};

typedef struct X509_POLICY_LEVEL_st X509_POLICY_LEVEL_st, *PX509_POLICY_LEVEL_st;

typedef struct X509_POLICY_LEVEL_st X509_POLICY_LEVEL;

struct X509_POLICY_LEVEL_st {
};

typedef struct DIST_POINT_st DIST_POINT;

typedef struct asn1_pctx_st ASN1_PCTX;

typedef struct X509_POLICY_NODE_st X509_POLICY_NODE_st, *PX509_POLICY_NODE_st;

typedef struct X509_POLICY_NODE_st X509_POLICY_NODE;

struct X509_POLICY_NODE_st {
};

typedef struct rand_meth_st rand_meth_st, *Prand_meth_st;

struct rand_meth_st {
    void (* seed)(void *, int);
    int (* bytes)(uchar *, int);
    void (* cleanup)(void);
    void (* add)(void *, int, double);
    int (* pseudorand)(uchar *, int);
    int (* status)(void);
};

typedef int (CRYPTO_EX_dup)(CRYPTO_EX_DATA *, CRYPTO_EX_DATA *, void *, int, long, void *);

typedef struct rand_meth_st RAND_METHOD;

typedef struct MD5state_st MD5state_st, *PMD5state_st;

typedef struct MD5state_st MD5_CTX;

struct MD5state_st {
    uint A;
    uint B;
    uint C;
    uint D;
    uint Nl;
    uint Nh;
    uint data[16];
    uint num;
};

typedef struct stack_st_OPENSSL_STRING stack_st_OPENSSL_STRING, *Pstack_st_OPENSSL_STRING;

struct stack_st_OPENSSL_STRING {
    _STACK stack;
};

typedef struct ERR_string_data_st ERR_string_data_st, *PERR_string_data_st;

typedef struct ERR_string_data_st ERR_STRING_DATA;

struct ERR_string_data_st {
    ulong error;
    char * string;
};

typedef struct evp_Encode_Ctx_st evp_Encode_Ctx_st, *Pevp_Encode_Ctx_st;

typedef struct evp_Encode_Ctx_st EVP_ENCODE_CTX;

struct evp_Encode_Ctx_st {
    int num;
    int length;
    uchar enc_data[80];
    int line_num;
    int expect_nl;
};

typedef int (EVP_PBE_KEYGEN)(EVP_CIPHER_CTX *, char *, int, ASN1_TYPE *, EVP_CIPHER *, EVP_MD *, int);

typedef int (EVP_PKEY_gen_cb)(EVP_PKEY_CTX *);

typedef struct drbg_ctx_st drbg_ctx_st, *Pdrbg_ctx_st;

typedef struct drbg_ctx_st DRBG_CTX;

struct drbg_ctx_st {
};

typedef struct stack_st_ASN1_TYPE ASN1_SEQUENCE_ANY;

typedef struct BIT_STRING_BITNAME_st BIT_STRING_BITNAME_st, *PBIT_STRING_BITNAME_st;

typedef struct BIT_STRING_BITNAME_st BIT_STRING_BITNAME;

struct BIT_STRING_BITNAME_st {
    int bitnum;
    char * lname;
    char * sname;
};

typedef struct ASN1_TLC_st ASN1_TLC_st, *PASN1_TLC_st;

typedef struct ASN1_TLC_st ASN1_TLC;

struct ASN1_TLC_st {
    char valid;
    int ret;
    long plen;
    int ptag;
    int pclass;
    int hdrlen;
};

typedef void * (d2i_of_void)(void * *, uchar * *, long);

typedef struct asn1_string_table_st asn1_string_table_st, *Pasn1_string_table_st;

struct asn1_string_table_st {
    int nid;
    long minsize;
    long maxsize;
    ulong mask;
    ulong flags;
};

typedef int (i2d_of_void)(void *, uchar * *);

typedef struct asn1_string_table_st ASN1_STRING_TABLE;

typedef union _union_1012 _union_1012, *P_union_1012;

union _union_1012 {
    uchar c[64];
    double q[64];
};

typedef struct WHIRLPOOL_CTX WHIRLPOOL_CTX, *PWHIRLPOOL_CTX;

struct WHIRLPOOL_CTX {
    union _union_1012 H;
    uchar data[64];
    uint bitoff;
    size_t bitlen[32];
};

typedef struct timezone timezone, *Ptimezone;

struct timezone {
    int tz_minuteswest;
    int tz_dsttime;
};

typedef __clockid_t clockid_t;

typedef struct timezone * __timezone_ptr_t;

typedef struct tm tm, *Ptm;

struct tm {
    int tm_sec;
    int tm_min;
    int tm_hour;
    int tm_mday;
    int tm_mon;
    int tm_year;
    int tm_wday;
    int tm_yday;
    int tm_isdst;
    long tm_gmtoff;
    char * tm_zone;
};

typedef union _union_714 _union_714, *P_union_714;

typedef uint KEY_TABLE_TYPE[68];

union _union_714 {
    double d;
    KEY_TABLE_TYPE rd_key;
};

typedef struct camellia_key_st camellia_key_st, *Pcamellia_key_st;

typedef struct camellia_key_st CAMELLIA_KEY;

struct camellia_key_st {
    union _union_714 u;
    int grand_rounds;
};

typedef long __fd_mask;

typedef struct fd_set fd_set, *Pfd_set;

struct fd_set {
    __fd_mask fds_bits[128];
};

typedef struct ocsp_basic_response_st ocsp_basic_response_st, *Pocsp_basic_response_st;

typedef struct ocsp_basic_response_st OCSP_BASICRESP;

typedef struct ocsp_response_data_st ocsp_response_data_st, *Pocsp_response_data_st;

typedef struct ocsp_response_data_st OCSP_RESPDATA;

typedef struct stack_st_OCSP_SINGLERESP stack_st_OCSP_SINGLERESP, *Pstack_st_OCSP_SINGLERESP;

struct ocsp_basic_response_st {
    OCSP_RESPDATA * tbsResponseData;
    X509_ALGOR * signatureAlgorithm;
    ASN1_BIT_STRING * signature;
    struct stack_st_X509 * certs;
};

struct stack_st_OCSP_SINGLERESP {
    _STACK stack;
};

struct ocsp_response_data_st {
    ASN1_INTEGER * version;
    OCSP_RESPID * responderId;
    ASN1_GENERALIZEDTIME * producedAt;
    struct stack_st_OCSP_SINGLERESP * responses;
    struct stack_st_X509_EXTENSION * responseExtensions;
};

typedef struct ocsp_service_locator_st ocsp_service_locator_st, *Pocsp_service_locator_st;

typedef struct ocsp_service_locator_st OCSP_SERVICELOC;

struct ocsp_service_locator_st {
    X509_NAME * issuer;
    struct stack_st_ACCESS_DESCRIPTION * locator;
};

typedef struct stack_st_OCSP_ONEREQ stack_st_OCSP_ONEREQ, *Pstack_st_OCSP_ONEREQ;

struct stack_st_OCSP_ONEREQ {
    _STACK stack;
};

typedef struct ocsp_signature_st ocsp_signature_st, *Pocsp_signature_st;

typedef struct ocsp_signature_st OCSP_SIGNATURE;

struct ocsp_signature_st {
    X509_ALGOR * signatureAlgorithm;
    ASN1_BIT_STRING * signature;
    struct stack_st_X509 * certs;
};

typedef struct ocsp_one_request_st ocsp_one_request_st, *Pocsp_one_request_st;

typedef struct ocsp_one_request_st OCSP_ONEREQ;

typedef struct ocsp_cert_id_st ocsp_cert_id_st, *Pocsp_cert_id_st;

typedef struct ocsp_cert_id_st OCSP_CERTID;

struct ocsp_cert_id_st {
    X509_ALGOR * hashAlgorithm;
    ASN1_OCTET_STRING * issuerNameHash;
    ASN1_OCTET_STRING * issuerKeyHash;
    ASN1_INTEGER * serialNumber;
};

struct ocsp_one_request_st {
    OCSP_CERTID * reqCert;
    struct stack_st_X509_EXTENSION * singleRequestExtensions;
};

typedef struct ocsp_revoked_info_st ocsp_revoked_info_st, *Pocsp_revoked_info_st;

typedef struct ocsp_revoked_info_st OCSP_REVOKEDINFO;

struct ocsp_revoked_info_st {
    ASN1_GENERALIZEDTIME * revocationTime;
    ASN1_ENUMERATED * revocationReason;
};

typedef struct ocsp_req_info_st ocsp_req_info_st, *Pocsp_req_info_st;

typedef struct ocsp_req_info_st OCSP_REQINFO;

struct ocsp_req_info_st {
    ASN1_INTEGER * version;
    GENERAL_NAME * requestorName;
    struct stack_st_OCSP_ONEREQ * requestList;
    struct stack_st_X509_EXTENSION * requestExtensions;
};

typedef struct ocsp_single_response_st ocsp_single_response_st, *Pocsp_single_response_st;

typedef struct ocsp_cert_status_st ocsp_cert_status_st, *Pocsp_cert_status_st;

typedef struct ocsp_cert_status_st OCSP_CERTSTATUS;

typedef union _union_962 _union_962, *P_union_962;

struct ocsp_single_response_st {
    OCSP_CERTID * certId;
    OCSP_CERTSTATUS * certStatus;
    ASN1_GENERALIZEDTIME * thisUpdate;
    ASN1_GENERALIZEDTIME * nextUpdate;
    struct stack_st_X509_EXTENSION * singleExtensions;
};

union _union_962 {
    ASN1_NULL * good;
    OCSP_REVOKEDINFO * revoked;
    ASN1_NULL * unknown;
};

struct ocsp_cert_status_st {
    int type;
    union _union_962 value;
};

typedef struct ocsp_request_st ocsp_request_st, *Pocsp_request_st;

typedef struct ocsp_request_st OCSP_REQUEST;

struct ocsp_request_st {
    OCSP_REQINFO * tbsRequest;
    OCSP_SIGNATURE * optionalSignature;
};

typedef struct ocsp_single_response_st OCSP_SINGLERESP;

typedef struct ocsp_crl_id_st ocsp_crl_id_st, *Pocsp_crl_id_st;

typedef struct ocsp_crl_id_st OCSP_CRLID;

struct ocsp_crl_id_st {
    ASN1_IA5STRING * crlUrl;
    ASN1_INTEGER * crlNum;
    ASN1_GENERALIZEDTIME * crlTime;
};

typedef enum Elf64_DynTag {
    DT_ANDROID_REL=1610612751,
    DT_ANDROID_RELA=1610612753,
    DT_ANDROID_RELASZ=1610612754,
    DT_ANDROID_RELR=1879040000,
    DT_ANDROID_RELRENT=1879040003,
    DT_ANDROID_RELRSZ=1879040001,
    DT_ANDROID_RELSZ=1610612752,
    DT_AUDIT=1879047932,
    DT_AUXILIARY=2147483645,
    DT_BIND_NOW=24,
    DT_CHECKSUM=1879047672,
    DT_CONFIG=1879047930,
    DT_DEBUG=21,
    DT_DEPAUDIT=1879047931,
    DT_FEATURE_1=1879047676,
    DT_FILTER=2147483647,
    DT_FINI=13,
    DT_FINI_ARRAY=26,
    DT_FINI_ARRAYSZ=28,
    DT_FLAGS=30,
    DT_FLAGS_1=1879048187,
    DT_GNU_CONFLICT=1879047928,
    DT_GNU_CONFLICTSZ=1879047670,
    DT_GNU_HASH=1879047925,
    DT_GNU_LIBLIST=1879047929,
    DT_GNU_LIBLISTSZ=1879047671,
    DT_GNU_PRELINKED=1879047669,
    DT_HASH=4,
    DT_INIT=12,
    DT_INIT_ARRAY=25,
    DT_INIT_ARRAYSZ=27,
    DT_JMPREL=23,
    DT_MOVEENT=1879047674,
    DT_MOVESZ=1879047675,
    DT_MOVETAB=1879047934,
    DT_NEEDED=1,
    DT_NULL=0,
    DT_PLTGOT=3,
    DT_PLTPAD=1879047933,
    DT_PLTPADSZ=1879047673,
    DT_PLTREL=20,
    DT_PLTRELSZ=2,
    DT_POSFLAG_1=1879047677,
    DT_PREINIT_ARRAY=32,
    DT_PREINIT_ARRAYSZ=33,
    DT_REL=17,
    DT_RELA=7,
    DT_RELACOUNT=1879048185,
    DT_RELAENT=9,
    DT_RELASZ=8,
    DT_RELCOUNT=1879048186,
    DT_RELENT=19,
    DT_RELR=36,
    DT_RELRENT=37,
    DT_RELRSZ=35,
    DT_RELSZ=18,
    DT_RPATH=15,
    DT_RUNPATH=29,
    DT_SONAME=14,
    DT_STRSZ=10,
    DT_STRTAB=5,
    DT_SYMBOLIC=16,
    DT_SYMENT=11,
    DT_SYMINENT=1879047679,
    DT_SYMINFO=1879047935,
    DT_SYMINSZ=1879047678,
    DT_SYMTAB=6,
    DT_TEXTREL=22,
    DT_TLSDESC_GOT=1879047927,
    DT_TLSDESC_PLT=1879047926,
    DT_VERDEF=1879048188,
    DT_VERDEFNUM=1879048189,
    DT_VERNEED=1879048190,
    DT_VERNEEDNUM=1879048191,
    DT_VERSYM=1879048176
} Elf64_DynTag;

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
};

typedef enum Elf_ProgramHeaderType {
    PT_DYNAMIC=2,
    PT_GNU_EH_FRAME=1685382480,
    PT_GNU_RELRO=1685382482,
    PT_GNU_STACK=1685382481,
    PT_INTERP=3,
    PT_LOAD=1,
    PT_NOTE=4,
    PT_NULL=0,
    PT_PHDR=6,
    PT_SHLIB=5,
    PT_TLS=7
} Elf_ProgramHeaderType;

typedef struct Elf64_Phdr Elf64_Phdr, *PElf64_Phdr;

struct Elf64_Phdr {
    enum Elf_ProgramHeaderType p_type;
    dword p_flags;
    qword p_offset;
    qword p_vaddr;
    qword p_paddr;
    qword p_filesz;
    qword p_memsz;
    qword p_align;
};

typedef struct Elf64_Shdr Elf64_Shdr, *PElf64_Shdr;

typedef enum Elf_SectionHeaderType {
    SHT_ANDROID_REL=1610612737,
    SHT_ANDROID_RELA=1610612738,
    SHT_CHECKSUM=1879048184,
    SHT_DYNAMIC=6,
    SHT_DYNSYM=11,
    SHT_FINI_ARRAY=15,
    SHT_GNU_ATTRIBUTES=1879048181,
    SHT_GNU_HASH=1879048182,
    SHT_GNU_LIBLIST=1879048183,
    SHT_GNU_verdef=1879048189,
    SHT_GNU_verneed=1879048190,
    SHT_GNU_versym=1879048191,
    SHT_GROUP=17,
    SHT_HASH=5,
    SHT_INIT_ARRAY=14,
    SHT_NOBITS=8,
    SHT_NOTE=7,
    SHT_NULL=0,
    SHT_PREINIT_ARRAY=16,
    SHT_PROGBITS=1,
    SHT_REL=9,
    SHT_RELA=4,
    SHT_SHLIB=10,
    SHT_STRTAB=3,
    SHT_SUNW_COMDAT=1879048187,
    SHT_SUNW_move=1879048186,
    SHT_SUNW_syminfo=1879048188,
    SHT_SYMTAB=2,
    SHT_SYMTAB_SHNDX=18
} Elf_SectionHeaderType;

struct Elf64_Shdr {
    dword sh_name;
    enum Elf_SectionHeaderType sh_type;
    qword sh_flags;
    qword sh_addr;
    qword sh_offset;
    qword sh_size;
    dword sh_link;
    dword sh_info;
    qword sh_addralign;
    qword sh_entsize;
};

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

typedef struct Gnu_BuildId Gnu_BuildId, *PGnu_BuildId;

struct Gnu_BuildId {
    dword namesz; // Length of name field
    dword descsz; // Length of description field
    dword type; // Vendor specific type
    char name[4]; // Build-id vendor name
    byte description[20]; // Build-id value
};

typedef struct Elf64_Ehdr Elf64_Ehdr, *PElf64_Ehdr;

struct Elf64_Ehdr {
    byte e_ident_magic_num;
    char e_ident_magic_str[3];
    byte e_ident_class;
    byte e_ident_data;
    byte e_ident_version;
    byte e_ident_osabi;
    byte e_ident_abiversion;
    byte e_ident_pad[7];
    word e_type;
    word e_machine;
    dword e_version;
    qword e_entry;
    qword e_phoff;
    qword e_shoff;
    dword e_flags;
    word e_ehsize;
    word e_phentsize;
    word e_phnum;
    word e_shentsize;
    word e_shnum;
    word e_shstrndx;
};




undefined8
aes_ocb_cipher(long param_1,undefined8 param_2,ulong *param_3,ulong param_4,undefined8 param_5,
              ulong param_6)

{
  int iVar1;
  undefined8 uVar2;
  
  uVar2 = ossl_prov_is_running();
  if ((int)uVar2 != 0) {
    if (param_4 < param_6) {
      ERR_new();
      ERR_set_debug("providers/implementations/ciphers/cipher_aes_ocb.c",0x1fa,"aes_ocb_cipher");
      ERR_set_error(0x39,0x6a,0);
      return 0;
    }
    if ((*(byte *)(param_1 + 0x3c) & 2) == 0) {
      iVar1 = CRYPTO_ocb128_decrypt(param_1 + 0x2b0,param_5,param_2,param_6);
    }
    else {
      iVar1 = CRYPTO_ocb128_encrypt();
    }
    if (iVar1 == 0) {
      ERR_new();
      ERR_set_debug("providers/implementations/ciphers/cipher_aes_ocb.c",0x1ff,"aes_ocb_cipher");
      ERR_set_error(0x39,0x66,0);
      return 0;
    }
    *param_3 = param_6;
    uVar2 = 1;
  }
  return uVar2;
}

int main(int param_1, const char *param_2[]){}
