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
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
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

typedef ushort sa_family_t;

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
typedef struct drbg_ctx_st drbg_ctx_st, *Pdrbg_ctx_st;

typedef struct drbg_ctx_st DRBG_CTX;

struct drbg_ctx_st {
};

typedef struct stat64 stat64, *Pstat64;

typedef ulong __dev_t;

typedef ulong __ino64_t;

typedef ulong __nlink_t;

typedef uint __mode_t;

typedef uint __uid_t;

typedef uint __gid_t;

typedef long __blksize_t;

typedef long __blkcnt64_t;

typedef struct timespec timespec, *Ptimespec;

typedef long __time_t;

struct timespec {
    __time_t tv_sec;
    long tv_nsec;
};

struct stat64 {
    __dev_t st_dev;
    __ino64_t st_ino;
    __nlink_t st_nlink;
    __mode_t st_mode;
    __uid_t st_uid;
    __gid_t st_gid;
    int __pad0;
    __dev_t st_rdev;
    __off_t st_size;
    __blksize_t st_blksize;
    __blkcnt64_t st_blocks;
    struct timespec st_atim;
    struct timespec st_mtim;
    struct timespec st_ctim;
    long __unused[3];
};

typedef int __clockid_t;

typedef __clockid_t clockid_t;

typedef struct timeval timeval, *Ptimeval;

typedef long __suseconds_t;

struct timeval {
    __time_t tv_sec;
    __suseconds_t tv_usec;
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

typedef long __clock_t;

typedef __clock_t clock_t;

typedef __time_t time_t;

typedef struct protoent protoent, *Pprotoent;

struct protoent {
    char * p_name;
    char * * p_aliases;
    int p_proto;
};

typedef struct servent servent, *Pservent;

struct servent {
    char * s_name;
    char * * s_aliases;
    int s_port;
    char * s_proto;
};

typedef struct _IO_FILE FILE;

typedef struct sockaddr sockaddr, *Psockaddr;

struct sockaddr {
    sa_family_t sa_family;
    char sa_data[14];
};

typedef uint __socklen_t;

typedef __socklen_t socklen_t;

typedef long __fd_mask;

typedef struct fd_set fd_set, *Pfd_set;

struct fd_set {
    __fd_mask fds_bits[128];
};

typedef long __ssize_t;

typedef __ssize_t ssize_t;

typedef int __pid_t;

typedef int __int32_t;

typedef ulong __cpu_mask;

typedef struct cpu_set_t cpu_set_t, *Pcpu_set_t;

struct cpu_set_t {
    __cpu_mask __bits[128];
};

typedef void (* __sighandler_t)(int);

typedef struct evp_pkey_ctx_st evp_pkey_ctx_st, *Pevp_pkey_ctx_st;

struct evp_pkey_ctx_st {
};

typedef struct evp_pkey_ctx_st EVP_PKEY_CTX;

typedef union pthread_attr_t pthread_attr_t, *Ppthread_attr_t;

union pthread_attr_t {
    char __size[56];
    long __align;
};

typedef ulong pthread_t;

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

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};

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




ulong checksum_ipv6(undefined *param_1,undefined *param_2,uint param_3,undefined8 param_4,
                   long param_5)

{
  undefined *puVar1;
  undefined *puVar2;
  undefined uVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  uint uVar7;
  ulong uVar8;
  
  uVar8 = (ulong)param_3;
  iVar5 = 0;
  puVar1 = param_1 + 0x10;
  do {
    uVar3 = *param_1;
    puVar2 = param_1 + 1;
    param_1 = param_1 + 2;
    iVar5 = iVar5 + (uint)CONCAT11(uVar3,*puVar2);
  } while (param_1 != puVar1);
  puVar1 = param_2 + 0x10;
  iVar6 = 0;
  do {
    uVar3 = *param_2;
    puVar2 = param_2 + 1;
    param_2 = param_2 + 2;
    iVar6 = iVar6 + (uint)CONCAT11(uVar3,*puVar2);
  } while (puVar1 != param_2);
  iVar4 = _checksum_calculate(param_5,param_4);
  iVar4 = iVar5 + param_3 + (int)param_4 + iVar6 + iVar4;
  uVar7 = (uint)uVar8;
  if (uVar7 == 6) {
    uVar7 = iVar4 - (uint)(ushort)(*(ushort *)(param_5 + 0x10) << 8 |
                                  *(ushort *)(param_5 + 0x10) >> 8);
  }
  else {
    if (uVar7 < 7) {
      if (uVar7 == 0) goto LAB_0014c502;
      if (uVar7 != 1) {
LAB_0014c52e:
        uVar8 = 0xffffffff;
        goto LAB_0014c502;
      }
    }
    else {
      if (uVar7 == 0x11) {
        uVar7 = iVar4 - (uint)(ushort)(*(ushort *)(param_5 + 6) << 8 | *(ushort *)(param_5 + 6) >> 8
                                      );
        goto LAB_0014c4e5;
      }
      if (uVar7 != 0x3a) goto LAB_0014c52e;
    }
    uVar7 = iVar4 - (uint)(ushort)(*(ushort *)(param_5 + 2) << 8 | *(ushort *)(param_5 + 2) >> 8);
  }
LAB_0014c4e5:
  uVar7 = (uVar7 & 0xffff) + (uVar7 >> 0x10);
  uVar8 = (ulong)(~((uVar7 & 0xffff) + (uVar7 >> 0x10)) & 0xffff);
LAB_0014c502:
  return uVar8 & 0xffffffff;
}

int main(int param_1, const char *param_2[]){}
