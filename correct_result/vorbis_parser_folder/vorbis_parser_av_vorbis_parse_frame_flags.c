typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned char    undefined1;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    word;
typedef struct Elf64_Rela Elf64_Rela, *PElf64_Rela;

struct Elf64_Rela {
    qword r_offset; // location to apply the relocation action
    qword r_info; // the symbol table index and the type of relocation
    qword r_addend; // a constant addend used to compute the relocatable field value
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




int av_vorbis_parse_frame_flags(long param_1,byte *param_2,int param_3,uint *param_4)

{
  byte bVar1;
  int iVar2;
  int iVar3;
  
  if ((*(int *)(param_1 + 0xc) == 0) || (param_3 < 1)) {
    return 0;
  }
  bVar1 = *param_2;
  if ((bVar1 & 1) == 0) {
    if (*(int *)(param_1 + 0x11c) == 1) {
      iVar3 = 0;
    }
    else {
      iVar3 = (int)(*(uint *)(param_1 + 0x120) & (uint)bVar1) >> 1;
      if (*(int *)(param_1 + 0x11c) <= iVar3) {
        av_log(param_1,0x10,"Invalid mode in packet\n");
        return -0x41444e49;
      }
    }
    iVar2 = *(int *)(param_1 + 0x18);
    iVar3 = *(int *)(param_1 + 0x1c + (long)iVar3 * 4);
    if (iVar3 != 0) {
      iVar2 = *(int *)(param_1 + ((ulong)((*(uint *)(param_1 + 0x124) & (uint)bVar1) != 0) + 4) * 4)
      ;
    }
    iVar3 = *(int *)(param_1 + 0x10 + (long)iVar3 * 4);
    *(int *)(param_1 + 0x18) = iVar3;
    return iVar2 + iVar3 >> 2;
  }
  if (param_4 != (uint *)0x0) {
    if (bVar1 == 1) {
      *param_4 = *param_4 | 1;
      return 0;
    }
    if (bVar1 == 3) {
      *param_4 = *param_4 | 2;
      return 0;
    }
    if (bVar1 == 5) {
      *param_4 = *param_4 | 4;
      return 0;
    }
  }
  av_log(param_1,0x10,"Invalid packet\n");
  return -0x41444e49;
}
