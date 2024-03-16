typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned char    undefined1;
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




// WARNING: Could not reconcile some variable overlaps

uint av_cmp_i(undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4)

{
  uint uVar1;
  ushort local_28;
  ushort uStack38;
  ushort uStack36;
  ushort uStack34;
  ushort uStack32;
  ushort uStack30;
  ushort uStack28;
  short sStack26;
  ushort local_18;
  ushort uStack22;
  ushort uStack20;
  ushort uStack18;
  ushort uStack16;
  ushort uStack14;
  ushort uStack12;
  short sStack10;
  
  uStack38 = (ushort)((ulong)param_1 >> 0x10);
  uStack36 = (ushort)((ulong)param_1 >> 0x20);
  uStack34 = (ushort)((ulong)param_1 >> 0x30);
  uStack30 = (ushort)((ulong)param_2 >> 0x10);
  uStack28 = (ushort)((ulong)param_2 >> 0x20);
  sStack26 = (short)((ulong)param_2 >> 0x30);
  uStack22 = (ushort)((ulong)param_3 >> 0x10);
  uStack20 = (ushort)((ulong)param_3 >> 0x20);
  uStack18 = (ushort)((ulong)param_3 >> 0x30);
  uStack14 = (ushort)((ulong)param_4 >> 0x10);
  uStack12 = (ushort)((ulong)param_4 >> 0x20);
  sStack10 = (short)((ulong)param_4 >> 0x30);
  uVar1 = (int)sStack26 - (int)sStack10;
  if ((((uVar1 == 0) && (uVar1 = (uint)uStack28 - (uint)uStack12, uVar1 == 0)) &&
      (uVar1 = (uint)uStack30 - (uint)uStack14, uVar1 == 0)) &&
     (((uStack16 = (ushort)param_4, uStack32 = (ushort)param_2,
       uVar1 = (uint)uStack32 - (uint)uStack16, uVar1 == 0 &&
       (uVar1 = (uint)uStack34 - (uint)uStack18, uVar1 == 0)) &&
      ((uVar1 = (uint)uStack36 - (uint)uStack20, uVar1 == 0 &&
       (uVar1 = (uint)uStack38 - (uint)uStack22, uVar1 == 0)))))) {
    local_28 = (ushort)param_1;
    local_18 = (ushort)param_3;
    uVar1 = (uint)local_28 - (uint)local_18;
    if (uVar1 == 0) {
      return uVar1;
    }
  }
  return (int)uVar1 >> 0x10 | 1;
}
