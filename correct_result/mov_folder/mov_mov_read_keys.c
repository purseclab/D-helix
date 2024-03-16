typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned int    uint;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    word;
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

typedef ulong size_t;




undefined8 mov_read_keys(long param_1,undefined8 param_2,undefined8 param_3,long param_4)

{
  long lVar1;
  uint uVar2;
  uint uVar3;
  int iVar4;
  long lVar5;
  undefined8 uVar6;
  uint uVar7;
  bool bVar8;
  
  if (param_4 < 8) {
    return 0;
  }
  avio_skip(param_2,4);
  uVar2 = avio_rb32();
  if (uVar2 < 0x1fffffff) {
    *(uint *)(param_1 + 0x38) = uVar2 + 1;
    lVar5 = av_mallocz((ulong)(uVar2 + 1) << 3);
    *(long *)(param_1 + 0x30) = lVar5;
    if (lVar5 == 0) {
      return 0xfffffff4;
    }
    if (uVar2 != 0) {
      lVar5 = 8;
      uVar7 = 1;
      do {
        uVar3 = avio_rb32(param_2);
        iVar4 = avio_rl32(param_2);
        if (uVar3 < 8) {
          av_log(*(undefined8 *)(param_1 + 8),0x10,"The key# %u in meta has invalid size:%u\n",uVar7
                 ,uVar3);
          return 0xbebbb1b7;
        }
        if (iVar4 != 0x6174646d) {
          avio_skip(param_2,uVar3 - 8);
        }
        lVar1 = *(long *)(param_1 + 0x30);
        uVar6 = av_mallocz(uVar3 - 7);
        *(undefined8 *)(lVar1 + lVar5) = uVar6;
        lVar1 = *(long *)(*(long *)(param_1 + 0x30) + lVar5);
        if (lVar1 == 0) {
          return 0xfffffff4;
        }
        lVar5 = lVar5 + 8;
        avio_read(param_2,lVar1,uVar3 - 8);
        bVar8 = uVar2 != uVar7;
        uVar7 = uVar7 + 1;
      } while (bVar8);
    }
    uVar6 = 0;
  }
  else {
    av_log(*(undefined8 *)(param_1 + 8),0x10,"The \'keys\' atom with the invalid key count: %u\n",
           uVar2);
    uVar6 = 0xbebbb1b7;
  }
  return uVar6;
}
