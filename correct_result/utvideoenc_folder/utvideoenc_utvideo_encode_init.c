typedef unsigned char   undefined;

typedef unsigned char    byte;
typedef unsigned char    dwfenc;
typedef unsigned int    dword;
typedef unsigned long    qword;
typedef unsigned long    ulong;
typedef unsigned char    undefined1;
typedef unsigned short    undefined2;
typedef unsigned int    undefined4;
typedef unsigned long    undefined8;
typedef unsigned short    ushort;
typedef unsigned short    word;
typedef ulong size_t;

typedef int (* __compar_fn_t)(void *, void *);

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




undefined8 utvideo_encode_init(long param_1)

{
  long lVar1;
  int iVar2;
  uint uVar3;
  undefined8 uVar4;
  long lVar5;
  char *pcVar6;
  undefined4 uVar7;
  int iVar8;
  long lVar9;
  
  uVar3 = *(uint *)(param_1 + 0x74);
  lVar1 = *(long *)(param_1 + 0x20);
  iVar8 = *(int *)(param_1 + 0x88);
  *(long *)(lVar1 + 8) = param_1;
  *(undefined4 *)(lVar1 + 0x70) = 4;
  *(long *)(lVar1 + 0xa0) = (long)(int)(uVar3 + 0x1f & 0xffffffe0);
  if (iVar8 == 5) {
    iVar8 = *(int *)(param_1 + 0x14c);
    *(undefined4 *)(lVar1 + 0x80) = 3;
    if (iVar8 == 1) {
      *(undefined4 *)(param_1 + 0x1c) = 0x34484c55;
      uVar7 = 0x34325659;
    }
    else {
      *(undefined4 *)(param_1 + 0x1c) = 0x34594c55;
      uVar7 = 0x34325659;
    }
  }
  else {
    if (iVar8 < 6) {
      if (iVar8 == 0) {
        if (((uVar3 & 1) != 0) || ((*(byte *)(param_1 + 0x78) & 1) != 0)) {
          pcVar6 = "4:2:0 video requires even width and height.\n";
LAB_0010132c:
          av_log(param_1,0x10,pcVar6);
          return 0xbebbb1b7;
        }
        iVar8 = *(int *)(param_1 + 0x14c);
        *(undefined4 *)(lVar1 + 0x80) = 3;
        if (iVar8 == 1) {
          *(undefined4 *)(param_1 + 0x1c) = 0x30484c55;
          uVar7 = 0x32315659;
        }
        else {
          *(undefined4 *)(param_1 + 0x1c) = 0x30594c55;
          uVar7 = 0x32315659;
        }
      }
      else {
        if (iVar8 != 4) goto LAB_001013a7;
        if ((uVar3 & 1) != 0) {
          pcVar6 = "4:2:2 video requires even width.\n";
          goto LAB_0010132c;
        }
        iVar8 = *(int *)(param_1 + 0x14c);
        *(undefined4 *)(lVar1 + 0x80) = 3;
        if (iVar8 == 1) {
          *(undefined4 *)(param_1 + 0x1c) = 0x32484c55;
          uVar7 = 0x32595559;
        }
        else {
          *(undefined4 *)(param_1 + 0x1c) = 0x32594c55;
          uVar7 = 0x32595559;
        }
      }
    }
    else {
      if (iVar8 == 0x47) {
        *(undefined4 *)(lVar1 + 0x80) = 3;
        uVar7 = 0x18010000;
        *(undefined4 *)(param_1 + 0x1c) = 0x47524c55;
      }
      else {
        if (iVar8 != 0x6f) {
LAB_001013a7:
          av_log(param_1,0x10,"Unknown pixel format: %d\n");
          return 0xbebbb1b7;
        }
        *(undefined4 *)(lVar1 + 0x80) = 4;
        uVar7 = 0x18020000;
        *(undefined4 *)(param_1 + 0x1c) = 0x41524c55;
        *(undefined4 *)(param_1 + 0x270) = 0x20;
      }
    }
  }
  ff_bswapdsp_init(lVar1 + 0x20);
  ff_llvidencdsp_init(lVar1 + 0x58);
  if (*(int *)(lVar1 + 0x90) == 2) {
    av_log(param_1,0x10,"Gradient prediction is not supported.\n");
    uVar4 = 0xabafb008;
  }
  else {
    if (*(uint *)(param_1 + 0x158) < 0x101) {
      iVar8 = *(int *)(param_1 + 0x78);
      lVar5 = av_pix_fmt_desc_get(*(undefined4 *)(param_1 + 0x88));
      iVar8 = iVar8 >> (*(byte *)(lVar5 + 10) & 0x1f);
      if (iVar8 < *(int *)(param_1 + 0x158)) {
        av_log(param_1,0x10,"Slice count %d is larger than the subsampling-applied height %d.\n",
               *(int *)(param_1 + 0x158),iVar8);
        uVar4 = 0xffffffea;
      }
      else {
        *(undefined4 *)(param_1 + 0x60) = 0x10;
        lVar9 = 0;
        lVar5 = av_mallocz(0x50);
        *(long *)(param_1 + 0x58) = lVar5;
        if (lVar5 == 0) {
          av_log(param_1,0x10,"Could not allocate extradata.\n");
          uVar4 = 0xfffffff4;
        }
        else {
          do {
            if (*(int *)(lVar1 + 0x80) == (int)lVar9 || *(int *)(lVar1 + 0x80) < (int)lVar9) {
              **(undefined4 **)(param_1 + 0x58) = 0x10000f0;
              *(undefined4 *)(*(long *)(param_1 + 0x58) + 4) = uVar7;
              *(undefined4 *)(*(long *)(param_1 + 0x58) + 8) = *(undefined4 *)(lVar1 + 0x70);
              if (*(int *)(param_1 + 0x158) == 0) {
                iVar2 = iVar8 / 0x78;
                if (iVar2 == 0) {
                  *(undefined4 *)(lVar1 + 0x84) = 1;
                }
                else {
                  if (0x7877 < iVar8) {
                    iVar2 = 0x100;
                  }
                  *(int *)(lVar1 + 0x84) = iVar2;
                }
              }
              else {
                *(int *)(lVar1 + 0x84) = *(int *)(param_1 + 0x158);
              }
              lVar5 = *(long *)(param_1 + 0x58);
              *(undefined4 *)(lVar1 + 0x88) = 1;
              uVar3 = (*(int *)(lVar1 + 0x84) + -1) * 0x1000000 | 1;
              *(uint *)(lVar1 + 0x74) = uVar3;
              *(uint *)(lVar5 + 0xc) = uVar3;
              return 0;
            }
            lVar5 = av_malloc((long)(*(int *)(param_1 + 0x78) + 2) * *(long *)(lVar1 + 0xa0) + 0x40)
            ;
            *(long *)(lVar1 + 0xb0 + lVar9 * 8) = lVar5;
            lVar9 = lVar9 + 1;
          } while (lVar5 != 0);
          av_log(param_1,0x10,"Cannot allocate temporary buffer 1.\n");
          uVar4 = 0xfffffff4;
        }
      }
    }
    else {
      av_log(param_1,0x10,
             "Slice count %d is not supported in Ut Video (theoretical range is 0-256).\n");
      uVar4 = 0xffffffea;
    }
  }
  return uVar4;
}
