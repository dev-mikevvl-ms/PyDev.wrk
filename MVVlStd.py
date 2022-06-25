# Distributed under the BSD license, version:BSD-3-Clause.
# Copyright © 2022 Mike Vl. Vlasov <dev.mikevvl@outlook.com>.
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# See:(https://opensource.org/licenses/BSD-3-Clause).

'''Mod:MVVlStd.py
Usa:
from MVVlStd import glSep_s, mInP_FltAVali_fefi
import MVVlStd
import mod.MVVlStd, mod.victory, mod.MyBankAcc
# MVVlStd.mInP_FltAVali_fefi('?')
# mInP_FltAVali_fefi('?')
  loMenu_o = mod.MVVlStd.mMenu_c(mMenu_d, **loKwArg_d)
'''
from distutils.command.build import build
import io, sys, time
from dataclasses import dataclass, field
from collections.abc import Callable
from typing import Any, Optional, Protocol, TypeAlias, TypeVar


glScrWid_i = 80
glSep_s = '_' *glScrWid_i

def mCre_SFrFloat_ff(laSrc_n:float, laReg_s:str='RU', la1kSep_s:str='_',
                     la1kSep4Frac_b:bool=True, laFracSepSv_b:bool=False, laLf0Sv_b:bool=True):
  if len(la1kSep_s) > 1 or la1kSep_s not in '.,_ ': la1kSep_s = '_'
  loRes_s, lo1kSepRPl_b = (f"{laSrc_n:_f}").rstrip('0'), None
  if la1kSep4Frac_b and loRes_s[-1] != '.':
    lo_l = loRes_s.split('.')
    lo_l[1] = '_'.join(lo_l[1][(0+_i)*3:(1+_i)*3] for _i in range(len(lo_l[1])//3 +1)
        if lo_l[1][(0+_i)*3:(1+_i)*3])
    loRes_s = '.'.join(lo_l)
  if laReg_s.lower() =='RU'.lower():
    loRes_s = loRes_s.replace('.', ',')
    if not laFracSepSv_b: loRes_s = loRes_s.rstrip(',')
    if la1kSep_s not in ',_' or la1kSep_s == '': lo1kSepRPl_b = True
  else:
    if not laFracSepSv_b: loRes_s = loRes_s.rstrip('.')
    if la1kSep_s not in '._' or la1kSep_s == '': lo1kSepRPl_b = True
    # return (f"{laSrc_n:{la1kSep_s}f}").rstrip('0').rstrip('.')
  if laLf0Sv_b and len(loRes_s) > 2 and loRes_s[0] == '0' and not loRes_s[1].isdecimal():
    loRes_s =loRes_s[1:]
  if lo1kSepRPl_b: return loRes_s.replace('_', la1kSep_s)
  else: return loRes_s

# tTs_t = tuple((_n, _Reg_s, _sep_s, _4Frac_b, _SepSv_b, _Lf0Sv_b, 
#   mCre_SFrFloat_ff(_n, laReg_s=_Reg_s, la1kSep_s=_sep_s, la1kSep4Frac_b=_4Frac_b,
#                    laFracSepSv_b=_SepSv_b, laLf0Sv_b=_Lf0Sv_b))
#   for _n in (1000.00, -122.444, 0.1598, 0, .5)
#   for _Reg_s in ('Ru', '') 
#   for _4Frac_b in (True, False) 
#   for _SepSv_b in (True, False) 
#   for _Lf0Sv_b in (True, False) 
#   for _sep_s in ('_', ' ', '', '.', ','))
# print(tuple(_el[-1] for _el in tTs_t))
# '''
# ('1_000,', '1 000,', '1000,', '1.000,', '1_000,', '1_000,', '1 000,', '1000,', '1.000,', '1_000,', '1_000', '1 000', '1000', '1.000', '1_000', '1_000', '1 000', '1000', '1.000', '1_000', '1_000,', '1 000,', '1000,', '1.000,', '1_000,', '1_000,', '1 000,', '1000,', '1.000,', '1_000,', '1_000', '1 000', '1000', '1.000', '1_000', '1_000', '1 000', '1000', '1.000', '1_000', '1_000.', '1 000.', '1000.', '1_000.', '1,000.', '1_000.', '1 000.', '1000.', '1_000.', '1,000.', '1_000', '1 000', '1000', '1_000', '1,000', '1_000', '1 000', '1000', '1_000', '1,000', '1_000.', '1 000.', '1000.', '1_000.', '1,000.', '1_000.', '1 000.', '1000.', '1_000.', '1,000.', '1_000', '1 000', '1000', '1_000', '1,000', '1_000', '1 000', '1000', '1_000', '1,000', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122,444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', '-122.444', ',159_8', ',159 8', ',1598', ',159.8', ',159_8', '0,159_8', '0,159 8', '0,1598', '0,159.8', '0,159_8', ',159_8', ',159 8', ',1598', ',159.8', ',159_8', '0,159_8', '0,159 8', '0,1598', '0,159.8', '0,159_8', ',1598', ',1598', ',1598', ',1598', ',1598', '0,1598', '0,1598', '0,1598', '0,1598', '0,1598', ',1598', ',1598', ',1598', ',1598', ',1598', '0,1598', '0,1598', '0,1598', '0,1598', '0,1598', '.159_8', '.159 8', '.1598', '.159_8', '.159,8', '0.159_8', '0.159 8', '0.1598', '0.159_8', '0.159,8', '.159_8', '.159 8', '.1598', '.159_8', '.159,8', '0.159_8', '0.159 8', '0.1598', '0.159_8', '0.159,8', '.1598', '.1598', '.1598', '.1598', '.1598', '0.1598', '0.1598', '0.1598', '0.1598', '0.1598', '.1598', '.1598', '.1598', '.1598', '.1598', '0.1598', '0.1598', '0.1598', '0.1598', '0.1598', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0,', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0.', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ',5', ',5', ',5', ',5', ',5', '0,5', '0,5', '0,5', '0,5', '0,5', ',5', ',5', ',5', ',5', ',5', '0,5', '0,5', '0,5', '0,5', '0,5', ',5', ',5', ',5', ',5', ',5', '0,5', '0,5', '0,5', '0,5', '0,5', ',5', ',5', ',5', ',5', ',5', '0,5', '0,5', '0,5', '0,5', '0,5', '.5', '.5', '.5', '.5', '.5', '0.5', '0.5', '0.5', '0.5', '0.5', '.5', '.5', '.5', '.5', '.5', '0.5', '0.5', '0.5', '0.5', '0.5', '.5', '.5', '.5', '.5', '.5', '0.5', '0.5', '0.5', '0.5', '0.5', '.5', '.5', '.5', '.5', '.5', '0.5', '0.5', '0.5', '0.5', '0.5')
# '''

mStdMsg4InP_t = (' Please, Input', ' and press Enter',
    'Your value will be validated as', 'on default ',
    # ' and {} attempt{} left'
    ' and {} attem. left',
    ' It remains to input {} more val.{}.')
mStdMsg4InP_t = (' Пожалуйста, введите', ' и нажмите Enter',
    'Ваш ввод должен соответствовать усл.', 'по умолчанию ',
    ' и осталось {} попыт.',
    ' Нужно ввести еще {} знач.{}.')
# 2Do:mInP_FltAVali_fefi->_c(...)
def mInP_FltAVali_fefi(laWhatInPMsg_s, laInPValues_co=1, laValiInPMsg_s='',
    laVali_cll=None, laInPTypeFlt_cll=int, laMaxInPTry_co=11,
    laAcceptEmptyInPAsDf_b=False, laDfV_s=None, laMsg4InP_l=mStdMsg4InP_t,
    laVerbose_i=None, file=sys.stdout) -> tuple:

  if laInPValues_co < 1: raise ValueError(f'laInPValues_co must be > 0, now:{laInPValues_co}')
  loTypeAValiFlsCo_l, loRes_l, loMaxTry_co = [0, 0], [], int(max(laInPValues_co, laMaxInPTry_co))
  if laValiInPMsg_s and laVali_cll:
    lo_s = f' - {laMsg4InP_l[2]}({laValiInPMsg_s}'
    if lo_s[-1] == '\n': lo_s = lo_s[:-1] + ') -\n'
    else: lo_s += ') -'
  else: lo_s = ''
  lo_s = laMsg4InP_l[0] + f"{laWhatInPMsg_s}{lo_s}" + laMsg4InP_l[1]
  if laAcceptEmptyInPAsDf_b and laDfV_s is not None:
    lo_s += f"({laMsg4InP_l[3]}'{laDfV_s}')"
  loInPMsg_s = f"{lo_s}: "

  for lo_co in range(loMaxTry_co):
    li_s = input(loInPMsg_s) # 2Do:try/except EOFError(Enter: ^Z)
    if li_s == '' and laAcceptEmptyInPAsDf_b and laDfV_s is not None:
      li_s = laDfV_s # 2Do: Che: laDfV_s is str OR UpLi
    # if not li_s: ??User(Exit|Bre) ??laAcceptEmpty(As(Df|Bre))InP_b=False
    try:
      if laInPTypeFlt_cll is not None:
        liChe_i = laInPTypeFlt_cll(li_s)
      else: liChe_i = li_s
    except ValueError as loExc_o:
      loTypeAValiFlsCo_l[0] +=1; liChe_i = None
      print(f"\tERR: You input:'{li_s}' NOT pass check type w/func({laInPTypeFlt_cll}",
          f'- Exception:{type(loExc_o).__name__}({loExc_o}) raised.', file=file)
    else:
      if laVali_cll is not None:
        if laVali_cll(liChe_i):
          loRes_l.append(liChe_i)
          # print(f"\tMSG: You input:'{liChe_i}' valid.", file=file)
        else:
          loTypeAValiFlsCo_l[1] +=1
          lo_s = f' because of NOT {laValiInPMsg_s}' if laValiInPMsg_s else ''
          print(f"\tERR: You input:'{liChe_i}' INVALID{lo_s}.", file=file)
      else:
        loRes_l.append(liChe_i)
        # print(f"\tMSG: You input:'{liChe_i}'.", file=file)
        # if liChe_i == tPtt_i: tOk_co +=1
    # print(f'DBG: {loRes_l=}')
    if len(loRes_l) == laInPValues_co: break  
    if laMaxInPTry_co:
      if lo_co == (loMaxTry_co -1): # RFa:Rm(NNe int)
        if loRes_l:
          print(f"\tWRN: Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co}, return {tuple(loRes_l)} as User input.", file=file)
        else:
          raise ValueError(f'Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co} but loRes_l is Empty - nothing return as User input.')
      else:
        # lo_s = '' if lo_co == (loMaxTry_co -2) else 's'
        # lo_s = f' and {loMaxTry_co - lo_co -1} attempt{lo_s} left'
        if laMsg4InP_l[-2]:
          lo_s = laMsg4InP_l[-2].format(loMaxTry_co - lo_co -1)
        else: lo_s = ''
    else: lo_s = '' #RFa:Rm:NNe(.rstrip('.'))
    if laMsg4InP_l[-1]:
      lo_s = laMsg4InP_l[-1].format(laInPValues_co - len(loRes_l), lo_s)
      print(lo_s.rstrip('.') + '.', file=file)
    # print(f'MSG: It remains to input {laInPValues_co - len(loRes_l)} more value{lo_s}.', file=file)
  return tuple(loRes_l)

# print(mod.MVVlStd.mInP_FltAVali_fefi(laWhatInPMsg_s=' Any Float', laInPValues_co=2, laInPTypeFlt_cll=float, laMaxInPTry_co=1),
#  mod.MVVlStd.mInP_FltAVali_fefi(' x', laValiInPMsg_s='x in (1,2,3)',
#   laVali_cll=lambda x: x in (1,2,3))
#   )
# print(mInP_FltAVali_fefi(laInPValues_co=2, laInPTypeFlt_cll=float, laMaxInPTry_co=1),
#  mInP_FltAVali_fefi(laValiWhatInPMsg_s=tCndInPMsg_s,
#   laVali_cll=lambda x: x in tValiV_t)
#   )
# t_s = '' if tOk_co == 1 else 's'
# print(f"You input '{tPtt_i}' {tOk_co} time{t_s} of {tTime_co} attempts.")

# tTime_co, tPtt_i, tOk_co, tFls_co = 10, 5, 0, 0

# tResLLen_co = int(mInP_FltAVali_fefi(laVali_cll=lambda _i: 0 < _i < 10,
#     laWhatInPMsg_s=' Количество элементов будущего списка',
#     laValiInPMsg_s=' a Integer 0 < _i < 10')[0],
#     )
# print(f'В списке будет {tResLLen_co} элементов.')
# tValiV_t = tuple(range(0, 10))
# tValiV_t = ('Y', 'N')
# tCndInPMsg_s = f' (по очереди по одной вводите любые цифры) a Integer OneOf{tValiV_t}'
# tRes_l = list(mInP_FltAVali_fefi(f' по очереди по одной любые цифры {tResLLen_co} раза',
#     laInPValues_co=tResLLen_co, laValiInPMsg_s=f'a Integer OneOf{tValiV_t}',
#     laVali_cll=lambda x: x in tValiV_t))
# tValiV_t = ('Y', 'N')
# tRes_l = list(mInP_FltAVali_fefi(f' Ts 2 times',
#     laInPValues_co=2, laInPTypeFlt_cll=None, laDfV_s='Y',
#     laAcceptEmptyInPAsDf_b=True, laValiInPMsg_s=f'a character OneOf{tValiV_t}',
#     laVali_cll=lambda _s: _s.upper() in tValiV_t))
# tRes_l.sort()
# print(tRes_l)
mT_ca = TypeVar("mT_ca")
mT_contra_ca = TypeVar("mT_contra_ca", contravariant=True)
mSelf_ca = TypeVar("mSelf_ca")
# mIntOStr_ca = TypeVar("mIntOStr_ca", int, str)

class mSupportsWrite_ca(Protocol[mT_contra_ca]):
    def write(self, __s: mT_contra_ca) -> object: ...

class mSupportsDunderLT_ca(Protocol):
    def __lt__(self, __other: Any) -> bool: ...
class mSupportsDunderGT_ca(Protocol):
    def __gt__(self, __other: Any) -> bool: ...
mSupportsRichComparison_ca: TypeAlias = mSupportsDunderLT_ca | mSupportsDunderGT_ca

mMenu_ca = TypeVar("mMenu_ca", bound="mMenu_c")
# mItmV_ca = TypeVar("mItmV_ca", list[str, Callable[[mMenu_ca, mSupportsWrite_ca | None], list],
#     Optional(Any)])
@dataclass
class mMenu_c():
  '''Class menu 
  '''
  fMenuItm_d: dict[int | str, list[
      tuple[str,
            Callable[[mMenu_ca, mSupportsWrite_ca], list],
            #  Callable[[mMenu_ca, mSupportsWrite_ca | None], list],
            # Optional(Any)]]] = field(default_factory=dict)
            Any | None]]]
  # ItmFmt(_k=Key, _v=[Desc_s, _cll, ??Aliases, ??ElType_en:(AlwOut_b, SvHst_b...)])
  # 2Do: ??Add(??fCaseInsens_b, ...)
  fAppTtl_s: str = ''
  fPrnOutStt_cll: Callable[[mMenu_ca, mSupportsWrite_ca], None] = None # OutVar # [self, file]; ??(Slv:NN)Df: IF fOutStt_d is !None -> print(fOutStt_d)
  # fPrnOutStt_cll: Callable[[mSelf_ca, mSupportsWrite_ca], None] = None # OutVar # [self, file]; ??(Slv:NN)Df: IF fOutStt_d is !None -> print(fOutStt_d)
  # fPrnOutStt_cll: Callable[[mMenu_ca, mSupportsWrite_ca | None], None] = None # OutVar # [self, file]; ??(Slv:NN)Df: IF fOutStt_d is !None -> print(fOutStt_d)
  fIterSortKey_cll: Callable[[mT_ca], mSupportsRichComparison_ca] = None # [key] ??(Prop4Set): AsIn2fOutMenuItm_d OR (lambda _el: str(_el))|int
  fHeaFmt_s: str = None
  fFooFmt_s: str = None
  fItmFmt_s: str = '{_k!s:>2}. {_v[0]}'
  fActHst_l: list[tuple[float, str, str, list]] = field(default_factory=list)
  # ElFmt:tuple(<time.time_ns()>, <Type_s>, <Desc_s|Cnt_a??>, <Ret_a>)
  # 2Do: SvHst_b, MaB:Get(Fr:fActHst_l):Ls(Ret_a)
  # 2Do: PP(Max(Col|Row)) 4 prn_fmp
  fAFile4Prn_o: mSupportsWrite_ca = sys.stdout

  def __post_init__(self):
    if self.fHeaFmt_s is not None: self.fHeaFmt_s = str(self.fHeaFmt_s)
    else:
      self.fHeaFmt_s = glSep_s
      if self.fAppTtl_s: self.fHeaFmt_s += f'\n{self.fAppTtl_s}:'
    if self.fFooFmt_s is not None: self.fFooFmt_s = str(self.fFooFmt_s)
    else: self.fFooFmt_s = glSep_s[:len(glSep_s)//3 *2]
    
    self.fRunLoop_b = bool(self.fMenuItm_d)
    self.fInP_s, self.fInP_k, self.fRes_a = None, None, None # 2Do:MaB:_f...
    if self.fActHst_l is not None:
      self.fActHst_l.append((time.time_ns(), 'Inn', '__post_init__', None))

  def __iter__(self): # 2Do: MaB Onl WhiUse(prn_fmp)
    if self.fIterSortKey_cll is None:
      return (_k for _k in self.fMenuItm_d.keys())
    return (_k for _k in sorted(self.fMenuItm_d.keys(), key=self.fIterSortKey_cll))

  def __getitem__(self, key): # BOf:KISS
    return self.fMenuItm_d[key]

  def __len__(self): # BOf:KISS
    return len(self.fMenuItm_d)

  def __contains__(self, key): # BOf:KISS
    return key in self.fMenuItm_d

  # 2Do: MaB: oup_fmp(self, file=fAFile4Prn_o)
  # 2Do: MaB Onl(9+KeyExit OR Fit2Scr+KeyExit) w/Set(sf.WhiVieItmKey_l)
  def prn_fmp(self, file=fAFile4Prn_o):
    if bool(self.fMenuItm_d):
      if self.fHeaFmt_s != '': print(self.fHeaFmt_s, file=file)
      print(*(self.fItmFmt_s.format(_k=_k, _v=self[_k]) for _k in self),
          sep='\n', file=file)
      self.prn_Info_fmp(file=file)
      if self.fFooFmt_s != '': print(self.fFooFmt_s, file=file)

  # 2Do: __str__(self), __format__, tVieHst_fmp
  def prn_Info_fmp(self, file=fAFile4Prn_o):
    if callable(self.fPrnOutStt_cll): #  #RFa:Rm:NNe(self.fPrnOutStt_cll and )
      self.fPrnOutStt_cll(self, file=file)

  # 2Do: add_Itms?_ffm(self), del_Itms?_ffpm(self), def get_Keys?_ffpm(self):
  # ??run_ffpm(self):
  def __call__(self, file=fAFile4Prn_o): # MainLoop
    if self.fActHst_l is not None:
      self.fActHst_l.append((time.time_ns(), 'Inn', 'Beg:MainLoop', None))
    while self.fRunLoop_b:
      self.prn_fmp(file=file)
      self.fInP_s, self.fInP_k = None, None # 2Do:MaB:Add:self.fRes_a
      try:
        self.fInP_s = mInP_FltAVali_fefi(f' пункт меню',
            laInPTypeFlt_cll=None, file=file)[0].strip()
      except EOFError as loExc_o:
        print(f'DVL:EOFError(Enter: ^Z):({loExc_o}).', file=file)
        self.fActHst_l.append((time.time_ns(), 'Inn',
            'End:MainLoop:BOf:EOFError(MaB:Enter: ^Z)', False))
        self.fRunLoop_b = False
        break
      if self.fInP_s in self:
        self.fInP_k = self.fInP_s
      else:
        try: self.fInP_k = int(self.fInP_s)
        except ValueError as loExc_o: self.fInP_k = None
        else:
          if self.fInP_k not in self: self.fInP_k = None
      if self.fInP_k is not None:
        lo_cll = self[self.fInP_k][1]
        if callable(lo_cll):
          self.fRes_a = lo_cll(self, file=file)
          if self.fActHst_l is not None:
            self.fActHst_l.append((time.time_ns(), 'InP',
                f'({self.fInP_s})' + self[self.fInP_k][0], self.fRes_a))
        else: # 2Do:??AddHst
          print(f'DVL: None 4 calling Fu() пункт меню({self.fInP_k})', file=file)
          continue
      else:
          print(f'MSG: Неверный пункт меню({self.fInP_s})', file=file) # 2Do:??AddHst
    else:
      if self.fHeaFmt_s != '': print(self.fHeaFmt_s, file=file)
      print('До свидания!', file=file)
      if self.fActHst_l is not None:
        self.fActHst_l.append((time.time_ns(), 'Inn', 'End:MainLoop', None))
      if self.fFooFmt_s != '': print(self.fFooFmt_s, file=file)

    return self.fActHst_l

# mMenu_c()