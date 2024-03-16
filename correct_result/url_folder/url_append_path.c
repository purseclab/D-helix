typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    ushort;
typedef unsigned short    word;
typedef ushort sa_family_t;

typedef struct sockaddr sockaddr, *Psockaddr;

struct sockaddr {
    sa_family_t sa_family;
    char sa_data[14];
};

typedef uint __socklen_t;

typedef __socklen_t socklen_t;

typedef ulong size_t;

typedef struct addrinfo addrinfo, *Paddrinfo;

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

typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
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

typedef struct Elf64_Sym Elf64_Sym, *PElf64_Sym;

struct Elf64_Sym {
    dword st_name;
    byte st_info;
    byte st_other;
    word st_shndx;
    qword st_value;
    qword st_size;
};




undefined8 append_path(void *param_1,long param_2,void **param_3,char *param_4,char *param_5)

{
  void *pvVar1;
  char *pcVar2;
  char cVar3;
  void *__dest;
  char *pcVar4;
  char local_51;
  
  __dest = *param_3;
  if (param_4 < param_5) {
    cVar3 = *param_4;
    pcVar4 = param_4;
    local_51 = cVar3;
    if (cVar3 == '/') {
      pcVar4 = param_4 + 1;
      if (param_5 <= pcVar4) goto LAB_001000d4;
      cVar3 = param_4[1];
      local_51 = cVar3;
      param_4 = pcVar4;
    }
LAB_0010005c:
    while (pcVar2 = strchr("/",(int)cVar3), pcVar2 == (char *)0x0) {
      pcVar4 = pcVar4 + 1;
      if (param_5 <= pcVar4) goto LAB_00100079;
      cVar3 = *pcVar4;
    }
    if (pcVar4 < param_5) {
      pcVar2 = pcVar4 + -(long)param_4;
      pcVar4 = pcVar4 + (cVar3 == '/');
      if (pcVar2 != (char *)0x1) goto LAB_0010008c;
LAB_00100111:
      if (local_51 != '.') goto LAB_00100096;
    }
    else {
LAB_00100079:
      pcVar2 = pcVar4 + -(long)param_4;
      if (pcVar2 == (char *)0x1) goto LAB_00100111;
LAB_0010008c:
      if (((pcVar2 == (char *)0x2) && (local_51 == '.')) && (param_4[1] == '.')) {
        pvVar1 = __dest;
        if (1 < (long)((long)__dest - (long)param_1)) {
          do {
            __dest = pvVar1;
            if (pvVar1 <= param_1) break;
            __dest = (void *)((long)pvVar1 - 1);
            pcVar2 = (char *)((long)pvVar1 - 2);
            pvVar1 = __dest;
          } while (*pcVar2 != '/');
        }
      }
      else {
LAB_00100096:
        pcVar2 = pcVar4 + -(long)param_4;
        if (param_2 - (long)__dest < (long)pcVar2) {
          return 0xfffffff4;
        }
        memmove(__dest,param_4,(size_t)pcVar2);
        __dest = (void *)((long)__dest + (long)pcVar2);
      }
    }
    if (pcVar4 < param_5) {
      cVar3 = *pcVar4;
      local_51 = cVar3;
      param_4 = pcVar4;
      goto LAB_0010005c;
    }
  }
LAB_001000d4:
  *param_3 = __dest;
  return 0;
}
