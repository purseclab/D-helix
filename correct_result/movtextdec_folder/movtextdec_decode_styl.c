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




undefined8 decode_styl(ushort *param_1,long param_2,long param_3)

{
  ushort *puVar1;
  ushort *puVar2;
  byte bVar3;
  long lVar4;
  undefined8 uVar5;
  ushort uVar6;
  uint uVar7;
  long lVar8;
  ushort uVar9;
  uint uVar10;
  
  uVar9 = *param_1 << 8 | *param_1 >> 8;
  uVar10 = (uint)uVar9;
  if ((ulong)(long)*(int *)(param_3 + 0x20) <
      (ulong)((long)*(int *)(param_2 + 0x60) + *(long *)(param_2 + 0x58) + 2 +
             (long)(int)(((uint)uVar9 + (uint)uVar9 * 2) * 4))) {
    uVar5 = 0xffffffff;
  }
  else {
    param_1 = param_1 + 1;
    lVar4 = av_realloc_array(*(undefined8 *)(param_2 + 8),uVar9,0x10);
    if (lVar4 != 0) {
      *(byte *)(param_2 + 0x50) = *(byte *)(param_2 + 0x50) | 1;
      uVar7 = 0;
      lVar8 = 0;
      *(long *)(param_2 + 8) = lVar4;
      *(ushort *)(param_2 + 0x52) = uVar9;
      if (uVar9 != 0) {
        do {
          while( true ) {
            puVar1 = (ushort *)(lVar4 + lVar8 * 0x10);
            uVar9 = *param_1 << 8 | *param_1 >> 8;
            *puVar1 = uVar9;
            uVar6 = param_1[1] << 8 | param_1[1] >> 8;
            puVar1[1] = uVar6;
            if ((uVar6 < uVar9) ||
               ((uVar7 != 0 &&
                (puVar2 = (ushort *)(lVar4 + -0xe + lVar8 * 0x10),
                uVar9 <= *puVar2 && *puVar2 != uVar9)))) {
              av_freep(param_2 + 8);
              *(undefined2 *)(param_2 + 0x52) = 0;
              return 0xfffffff4;
            }
            if (uVar6 == uVar9) break;
            uVar7 = uVar7 + 1;
            puVar1[7] = param_1[2] << 8 | param_1[2] >> 8;
            bVar3 = *(byte *)(param_1 + 3);
            *(byte *)(puVar1 + 2) = bVar3;
            *(byte *)((long)puVar1 + 5) = bVar3 & 1;
            *(byte *)((long)puVar1 + 7) = bVar3 >> 2 & 1;
            *(byte *)(puVar1 + 3) = bVar3 >> 1 & 1;
            *(undefined *)((long)puVar1 + 0xd) = *(undefined *)((long)param_1 + 7);
            *(uint *)(puVar1 + 4) =
                 (uint)*(byte *)(param_1 + 4) << 0x10 | (uint)*(byte *)((long)param_1 + 9) << 8 |
                 (uint)*(byte *)(param_1 + 5);
            *(undefined *)(puVar1 + 6) = *(undefined *)((long)param_1 + 0xb);
            uVar10 = (uint)*(ushort *)(param_2 + 0x52);
            if (*(ushort *)(param_2 + 0x52) == uVar7 || (int)uVar10 < (int)uVar7) {
              return 0;
            }
            lVar8 = (long)(int)uVar7;
            param_1 = param_1 + 6;
          }
          uVar10 = uVar10 - 1;
          *(short *)(param_2 + 0x52) = (short)uVar10;
          param_1 = param_1 + 6;
        } while ((int)uVar7 < (int)(uVar10 & 0xffff));
      }
      return 0;
    }
    uVar5 = 0xfffffff4;
  }
  return uVar5;
}
