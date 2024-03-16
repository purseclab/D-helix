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
typedef long long    longlong;
typedef unsigned long    qword;
typedef unsigned char    uchar;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned long long    ulonglong;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
typedef unsigned long    undefined6;
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

typedef ushort sa_family_t;

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

typedef void _IO_lock_t;

typedef struct _IO_marker _IO_marker, *P_IO_marker;

typedef struct _IO_FILE _IO_FILE, *P_IO_FILE;

typedef long __off_t;

typedef long __off64_t;

typedef ulong size_t;

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
/*
struct _IO_marker {
    struct _IO_marker * _next;
    struct _IO_FILE * _sbuf;
    int _pos;
};
*/
typedef struct stat stat, *Pstat;

typedef ulong __dev_t;

typedef ulong __ino_t;

typedef ulong __nlink_t;

typedef uint __mode_t;

typedef uint __uid_t;

typedef uint __gid_t;

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

typedef struct hmac_ctx_st hmac_ctx_st, *Phmac_ctx_st;

typedef struct hmac_ctx_st HMAC_CTX;

typedef struct env_md_st env_md_st, *Penv_md_st;

typedef struct env_md_ctx_st env_md_ctx_st, *Penv_md_ctx_st;

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

typedef int (pem_password_cb)(char *, int, int, void *);

typedef struct addrinfo addrinfo, *Paddrinfo;

typedef uint __socklen_t;

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

typedef struct stack_st_void stack_st_void, *Pstack_st_void;

typedef struct stack_st stack_st, *Pstack_st;

typedef struct stack_st _STACK;

struct stack_st {
    int num;
    char * * data;
    int sorted;
    int num_alloc;
    int (* comp)(void *, void *);
};

struct stack_st_void {
    _STACK stack;
};

typedef struct bio_st bio_st, *Pbio_st;

typedef struct bio_method_st bio_method_st, *Pbio_method_st;

typedef struct bio_st BIO;

typedef void (bio_info_cb)(struct bio_st *, int, char *, int, long, long);

typedef struct bio_method_st BIO_METHOD;

typedef struct crypto_ex_data_st crypto_ex_data_st, *Pcrypto_ex_data_st;

typedef struct crypto_ex_data_st CRYPTO_EX_DATA;

struct crypto_ex_data_st {
    struct stack_st_void * sk;
    int dummy;
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

typedef struct _IO_FILE FILE;

typedef long __ssize_t;

typedef __ssize_t ssize_t;

typedef int __pid_t;

typedef long __suseconds_t;

typedef int __clockid_t;

typedef struct pollfd pollfd, *Ppollfd;

struct pollfd {
    int fd;
    short events;
    short revents;
};

typedef ulong nfds_t;

typedef struct dh_method dh_method, *Pdh_method;

typedef struct dh_st dh_st, *Pdh_st;

typedef struct dh_st DH;

typedef struct bignum_st bignum_st, *Pbignum_st;

typedef struct bignum_st BIGNUM;

typedef struct bignum_ctx bignum_ctx, *Pbignum_ctx;

typedef struct bignum_ctx BN_CTX;

typedef struct bn_mont_ctx_st bn_mont_ctx_st, *Pbn_mont_ctx_st;

typedef struct bn_mont_ctx_st BN_MONT_CTX;

typedef struct bn_gencb_st bn_gencb_st, *Pbn_gencb_st;

typedef struct bn_gencb_st BN_GENCB;

typedef struct dh_method DH_METHOD;

typedef union _union_175 _union_175, *P_union_175;

union _union_175 {
    void (* cb_1)(int, int, void *);
    int (* cb_2)(int, int, BN_GENCB *);
};

struct bn_gencb_st {
    uint ver;
    void * arg;
    union _union_175 cb;
};

struct bignum_st {
    ulong * d;
    int top;
    int dmax;
    int neg;
    int flags;
};

struct bignum_ctx {
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

struct bn_mont_ctx_st {
    int ri;
    BIGNUM RR;
    BIGNUM N;
    BIGNUM Ni;
    ulong n0[2];
    int flags;
};

typedef struct asn1_string_st asn1_string_st, *Pasn1_string_st;

typedef struct asn1_string_st ASN1_T61STRING;

struct asn1_string_st {
    int length;
    int type;
    uchar * data;
    long flags;
};

typedef struct asn1_string_st ASN1_OCTET_STRING;

typedef struct asn1_string_st ASN1_GENERALSTRING;

typedef struct asn1_string_st ASN1_UTF8STRING;

typedef struct evp_pkey_asn1_method_st evp_pkey_asn1_method_st, *Pevp_pkey_asn1_method_st;

typedef struct evp_pkey_asn1_method_st EVP_PKEY_ASN1_METHOD;

struct evp_pkey_asn1_method_st {
};

typedef struct evp_pkey_st evp_pkey_st, *Pevp_pkey_st;

typedef struct evp_pkey_st EVP_PKEY;

typedef union _union_271 _union_271, *P_union_271;

typedef struct stack_st_X509_ATTRIBUTE stack_st_X509_ATTRIBUTE, *Pstack_st_X509_ATTRIBUTE;

typedef struct rsa_st rsa_st, *Prsa_st;

typedef struct dsa_st dsa_st, *Pdsa_st;

typedef struct ec_key_st ec_key_st, *Pec_key_st;

typedef struct rsa_meth_st rsa_meth_st, *Prsa_meth_st;

typedef struct rsa_st RSA;

typedef struct rsa_meth_st RSA_METHOD;

typedef struct bn_blinding_st bn_blinding_st, *Pbn_blinding_st;

typedef struct bn_blinding_st BN_BLINDING;

typedef struct dsa_method dsa_method, *Pdsa_method;

typedef struct DSA_SIG_st DSA_SIG_st, *PDSA_SIG_st;

typedef struct DSA_SIG_st DSA_SIG;

typedef struct dsa_st DSA;

typedef struct dsa_method DSA_METHOD;

struct ec_key_st {
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

struct bn_blinding_st {
};

union _union_271 {
    char * ptr;
    struct rsa_st * rsa;
    struct dsa_st * dsa;
    struct dh_st * dh;
    struct ec_key_st * ec;
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

struct stack_st_X509_ATTRIBUTE {
    _STACK stack;
};

struct DSA_SIG_st {
    BIGNUM * r;
    BIGNUM * s;
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

typedef struct evp_cipher_st evp_cipher_st, *Pevp_cipher_st;

typedef struct evp_cipher_ctx_st evp_cipher_ctx_st, *Pevp_cipher_ctx_st;

typedef struct evp_cipher_ctx_st EVP_CIPHER_CTX;

typedef struct asn1_type_st asn1_type_st, *Pasn1_type_st;

typedef struct asn1_type_st ASN1_TYPE;

typedef struct evp_cipher_st EVP_CIPHER;

typedef union _union_257 _union_257, *P_union_257;

typedef int ASN1_BOOLEAN;

typedef struct asn1_string_st ASN1_STRING;

typedef struct asn1_object_st asn1_object_st, *Pasn1_object_st;

typedef struct asn1_object_st ASN1_OBJECT;

typedef struct asn1_string_st ASN1_INTEGER;

typedef struct asn1_string_st ASN1_ENUMERATED;

typedef struct asn1_string_st ASN1_BIT_STRING;

typedef struct asn1_string_st ASN1_PRINTABLESTRING;

typedef struct asn1_string_st ASN1_IA5STRING;

typedef struct asn1_string_st ASN1_BMPSTRING;

typedef struct asn1_string_st ASN1_UNIVERSALSTRING;

typedef struct asn1_string_st ASN1_UTCTIME;

typedef struct asn1_string_st ASN1_GENERALIZEDTIME;

typedef struct asn1_string_st ASN1_VISIBLESTRING;

typedef struct ASN1_VALUE_st ASN1_VALUE_st, *PASN1_VALUE_st;

typedef struct ASN1_VALUE_st ASN1_VALUE;

struct ASN1_VALUE_st {
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

struct asn1_object_st {
    char * sn;
    char * * ln;
    int nid;
    int length;
    uchar * data;
    int flags;
};

typedef struct passwd passwd, *Ppasswd;

struct passwd {
    char * pw_name;
    char * pw_passwd;
    __uid_t pw_uid;
    __gid_t pw_gid;
    char * pw_gecos;
    char * pw_dir;
    char * pw_shell;
};

typedef struct dirent dirent, *Pdirent;

struct dirent {
    __ino_t d_ino;
    __off_t d_off;
    ushort d_reclen;
    uchar d_type;
    char d_name[256];
};

typedef union pthread_mutex_t pthread_mutex_t, *Ppthread_mutex_t;

typedef struct __pthread_mutex_s __pthread_mutex_s, *P__pthread_mutex_s;

typedef struct __pthread_internal_list __pthread_internal_list, *P__pthread_internal_list;

typedef struct __pthread_internal_list __pthread_list_t;

struct __pthread_internal_list {
    struct __pthread_internal_list * __prev;
    struct __pthread_internal_list * __next;
};

struct __pthread_mutex_s {
    int __lock;
    uint __count;
    int __owner;
    uint __nusers;
    int __kind;
    int __spins;
    __pthread_list_t __list;
};

union pthread_mutex_t {
    struct __pthread_mutex_s __data;
    char __size[40];
    long __align;
};

typedef union pthread_mutexattr_t pthread_mutexattr_t, *Ppthread_mutexattr_t;

union pthread_mutexattr_t {
    char __size[4];
    int __align;
};

typedef ulong pthread_t;

typedef struct glob_t glob_t, *Pglob_t;

struct glob_t {
    size_t gl_pathc;
    char * * gl_pathv;
    size_t gl_offs;
    int gl_flags;
    void (* gl_closedir)(void *);
    dirent * (* gl_readdir)(void *);
    void * (* gl_opendir)(char *);
    int (* gl_lstat)(char *, struct stat *);
    int (* gl_stat)(char *, struct stat *);
};

/*
typedef void * __gnuc_va_list;
*/

typedef struct timezone timezone, *Ptimezone;

struct timezone {
    int tz_minuteswest;
    int tz_dsttime;
};

typedef __time_t time_t;

typedef __clockid_t clockid_t;

typedef struct timeval timeval, *Ptimeval;

struct timeval {
    __time_t tv_sec;
    __suseconds_t tv_usec;
};

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

typedef struct ec_point_st ec_point_st, *Pec_point_st;

typedef struct ec_point_st EC_POINT;

struct ec_point_st {
};

typedef struct ec_key_st EC_KEY;

typedef enum enum_295 {
    POINT_CONVERSION_COMPRESSED=2,
    POINT_CONVERSION_HYBRID=6,
    POINT_CONVERSION_UNCOMPRESSED=4
} enum_295;

typedef enum enum_295 point_conversion_form_t;

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

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
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

typedef uint uint32_t;

typedef ushort uint16_t;




undefined4 sftp_get_new_id(char* param_1)

{
  *(int *)(param_1 + 0x28) = *(int *)(param_1 + 0x28) + 1;
  return *(undefined4 *)(param_1 + 0x28);
}

int main(int param_1, const char *param_2[]){}
