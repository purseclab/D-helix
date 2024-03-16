typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
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

typedef ulong size_t;




ulong bmv_read_packet(long param_1,long param_2)

{
  void **ppvVar1;
  void *pvVar2;
  void *pvVar3;
  uint uVar4;
  int iVar5;
  int iVar6;
  ulong uVar7;
  long lVar8;
  
  ppvVar1 = *(void ***)(param_1 + 0x18);
  do {
    if (*(int *)((long)ppvVar1 + 0xc) == 0) {
      iVar5 = *(int *)(ppvVar1 + 1);
      goto LAB_001000f8;
    }
    if (*(int *)(*(long *)(param_1 + 0x20) + 0x50) != 0) goto LAB_001001a0;
    uVar4 = avio_r8();
  } while (uVar4 == 0);
  if (uVar4 == 1) {
LAB_001001a0:
    uVar7 = 0xdfb9b0bb;
  }
  else {
    iVar5 = avio_rl24(*(undefined8 *)(param_1 + 0x20));
    *(int *)(ppvVar1 + 1) = iVar5;
    if (iVar5 == 0) {
      uVar7 = 0xbebbb1b7;
    }
    else {
      uVar7 = av_reallocp(ppvVar1,(long)(iVar5 + 1));
      if (-1 < (int)uVar7) {
        *(char *)*ppvVar1 = (char)uVar4;
        iVar6 = avio_read(*(undefined8 *)(param_1 + 0x20),(long)*ppvVar1 + 1,
                          *(undefined4 *)(ppvVar1 + 1));
        iVar5 = *(int *)(ppvVar1 + 1);
        if (iVar6 == iVar5) {
          if ((uVar4 & 0x20) == 0) {
LAB_001000f8:
            uVar7 = av_new_packet(param_2,iVar5 + 1);
            if (-1 < (int)uVar7) {
              *(undefined4 *)(param_2 + 0x24) = 0;
              pvVar2 = *(void **)(param_2 + 0x18);
              *(undefined4 *)((long)ppvVar1 + 0xc) = 1;
              memcpy(pvVar2,*ppvVar1,(long)*(int *)(param_2 + 0x20));
              return (ulong)*(uint *)(param_2 + 0x20);
            }
          }
          else {
            iVar5 = *(byte *)((long)*ppvVar1 + 1) + 1 + (uint)*(byte *)((long)*ppvVar1 + 1) * 0x40;
            if (iVar5 < iVar6) {
              uVar7 = av_new_packet(param_2);
              if (-1 < (int)uVar7) {
                memcpy(*(void **)(param_2 + 0x18),(void *)((long)*ppvVar1 + 1),
                       (long)*(int *)(param_2 + 0x20));
                pvVar2 = ppvVar1[2];
                pvVar3 = *ppvVar1;
                *(undefined4 *)(param_2 + 0x24) = 1;
                *(void **)(param_2 + 8) = pvVar2;
                lVar8 = (long)(int)((uint)*(byte *)((long)pvVar3 + 1) << 5);
                *(long *)(param_2 + 0x40) = lVar8;
                ppvVar1[2] = (void *)(lVar8 + (long)pvVar2);
                uVar4 = *(uint *)(param_2 + 0x20);
                *(undefined4 *)((long)ppvVar1 + 0xc) = 0;
                return (ulong)uVar4;
              }
            }
            else {
              av_log(param_1,0x10,"Reported audio size %d is bigger than packet size (%d)\n",iVar5,
                     iVar6);
              uVar7 = 0xbebbb1b7;
            }
          }
        }
        else {
          uVar7 = 0xfffffffb;
        }
      }
    }
  }
  return uVar7;
}
