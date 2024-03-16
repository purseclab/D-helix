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
int di_ino_hash; //add global variable by muqi
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
typedef unsigned int    undefined4;
typedef unsigned long    undefined5;
typedef unsigned long    undefined7;
typedef unsigned long    undefined8;
typedef unsigned short    ushort;
typedef int    wchar_t;
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

typedef ulong wctype_t;

typedef struct statfs statfs, *Pstatfs;

typedef ulong __fsblkcnt_t;

typedef ulong __fsfilcnt_t;

/*
typedef struct __fsid_t __fsid_t, *P__fsid_t;
*/

struct __fsid_t {
    int __val[2];
};

struct statfs {
    long f_type;
    long f_bsize;
    __fsblkcnt_t f_blocks;
    __fsblkcnt_t f_bfree;
    __fsblkcnt_t f_bavail;
    __fsfilcnt_t f_files;
    __fsfilcnt_t f_ffree;
    struct __fsid_t f_fsid;
    long f_namelen;
    long f_frsize;
    long f_flags;
    long f_spare[4];
};

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

typedef __time_t time_t;

typedef struct _IO_FILE FILE;

typedef uint wint_t;

typedef long __ssize_t;

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

struct evp_pkey_ctx_st {
};

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

typedef int nl_item;

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

/*
typedef struct __mbstate_t __mbstate_t, *P__mbstate_t;
*/

typedef union _union_27 _union_27, *P_union_27;

union _union_27 {
    uint __wch;
    char __wchb[4];
};

struct __mbstate_t {
    int __count;
    union _union_27 __value;
};

typedef struct __mbstate_t mbstate_t;

typedef int (* __compar_fn_t)(void *, void *);

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

typedef struct Elf64_Dyn Elf64_Dyn, *PElf64_Dyn;

struct Elf64_Dyn {
    enum Elf64_DynTag d_tag;
    qword d_val;
};

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
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

typedef ulong uintmax_t;

typedef long intmax_t;

typedef struct lconv lconv, *Plconv;

struct lconv {
    char * decimal_point;
    char * thousands_sep;
    char * grouping;
    char * int_curr_symbol;
    char * currency_symbol;
    char * mon_decimal_point;
    char * mon_thousands_sep;
    char * mon_grouping;
    char * positive_sign;
    char * negative_sign;
    char int_frac_digits;
    char frac_digits;
    char p_cs_precedes;
    char p_sep_by_space;
    char n_cs_precedes;
    char n_sep_by_space;
    char p_sign_posn;
    char n_sign_posn;
    char int_p_cs_precedes;
    char int_p_sep_by_space;
    char int_n_cs_precedes;
    char int_n_sep_by_space;
    char int_p_sign_posn;
    char int_n_sign_posn;
};




long map_device(undefined8 *param_1,char* param_2)

{
  long *plVar1;
  long lVar2;
  long *local_18;
  
  local_18 = (long *)param_1[2];
  if (local_18 == (long *)0x0) {
    local_18 = (long *)malloc(0x10);
    param_1[2] = local_18;
    if (local_18 == (long *)0x0) {
      return 0;
    }
  }
  else {
    if (param_2 == *local_18) {
      return local_18[1];
    }
  }
  *local_18 = param_2;
  plVar1 = (long *)hash_insert(*param_1,local_18);
  if (plVar1 == (long *)0x0) {
    lVar2 = 0;
  }
  else {
    if (plVar1 == local_18) {
      param_1[2] = 0;
      lVar2 = hash_initialize(0x3fd,0,di_ino_hash,0,0);
      local_18[1] = lVar2;
    }
    else {
      local_18[1] = plVar1[1];
    }
    lVar2 = local_18[1];
  }
  return lVar2;
}

int main(int param_1, const char *param_2[]){}
