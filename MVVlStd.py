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

# Mod:MVVlStd.py
# Usa:
# from MVVlStd import glSep_s, inp_FltAVali_fefi
# import MVVlStd
# # MVVlStd.inp_FltAVali_fefi('?')
# # inp_FltAVali_fefi('?')
import copy, sys, time
from dataclasses import dataclass, field
from collections.abc import Callable

glScrWid_s = 80
glSep_s = '_' *glScrWid_s

glStdMsg4InP_l = [' Please, Input', ' and press Enter',
    'Your value will be validated as', 'on default ',
    # ' and {} attempt{} left'
    ' and {} attem. left',
    ' It remains to input {} more val.{}.']
glStdMsg4InP_l = [' Пожалуйста, введите', ' и нажмите Enter',
    'Ваш ввод должен соответствовать усл.', 'по умолчанию ',
    ' и осталось {} попыт.',
    ' Нужно ввести еще {} знач.{}.']
def inp_FltAVali_fefi(laWhatInPMsg_s, laInPValues_co=1, laValiInPMsg_s='',
    laVali_cll=None, laInPTypeFlt_cll=int, laMaxInPTry_co=11,
    laAcceptEmptyInPAsDf_b=False, laDfV_s=None, laMsg4InP_l=glStdMsg4InP_l,
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
  for l_co in range(loMaxTry_co):
    li_s = input(loInPMsg_s)
    if li_s == '' and laAcceptEmptyInPAsDf_b and laDfV_s is not None:
      li_s = laDfV_s # 2Do: Che: laDfV_s is str OR UpLi
    # if not li_s: ??User(Exit|Bre) ??laAcceptEmpty(As(Df|Bre))InP_b=False
    try:
      if laInPTypeFlt_cll is not None:
        liChe_i = laInPTypeFlt_cll(li_s)
      else: liChe_i = li_s
    except ValueError as leExc_o:
      loTypeAValiFlsCo_l[0] +=1; liChe_i = None
      print(f"\tERR: You input:'{li_s}' NOT pass check type w/func({laInPTypeFlt_cll}",
          f'- Exception:{type(leExc_o).__name__}({leExc_o}) raised.', file=file)
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
      if l_co == int(loMaxTry_co -1):
        if loRes_l:
          print(f"\tWRN: Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co}, return {tuple(loRes_l)} as User input.", file=file)
        else:
          raise ValueError(f'Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co} but loRes_l is Empty - nothing return as User input.')
      else:
        # lo_s = '' if l_co == (loMaxTry_co -2) else 's'
        # lo_s = f' and {loMaxTry_co - l_co -1} attempt{lo_s} left'
        if laMsg4InP_l[-2]:
          lo_s = laMsg4InP_l[-2].format(loMaxTry_co - l_co -1)
        else: lo_s = ''
    else: lo_s = ''.rstrip('.')
    if laMsg4InP_l[-1]:
      lo_s = laMsg4InP_l[-1].format(laInPValues_co - len(loRes_l), lo_s)
      print(lo_s.rstrip('.') + '.', file=file)
    # print(f'MSG: It remains to input {laInPValues_co - len(loRes_l)} more value{lo_s}.', file=file)
  return tuple(loRes_l)
# print(inp_FltAVali_fefi(laInPValues_co=2, laInPTypeFlt_cll=float, laMaxInPTry_co=1),
#  inp_FltAVali_fefi(laValiWhatInPMsg_s=tCndInPMsg_s,
#   laVali_cll=lambda x: x in tValiV_t)
#   )
# t_s = '' if tOk_co == 1 else 's'
# print(f"You input '{tPtt_i}' {tOk_co} time{t_s} of {tTime_co} attempts.")

# tTime_co, tPtt_i, tOk_co, tFls_co = 10, 5, 0, 0

# tResLLen_co = int(inp_FltAVali_fefi(laVali_cll=lambda _i: 0 < _i < 10,
#     laWhatInPMsg_s=' Количество элементов будущего списка',
#     laValiInPMsg_s=' a Integer 0 < _i < 10')[0],
#     )
# print(f'В списке будет {tResLLen_co} элементов.')
# tValiV_t = tuple(range(0, 10))
# tValiV_t = ('Y', 'N')
# tCndInPMsg_s = f' (по очереди по одной вводите любые цифры) a Integer OneOf{tValiV_t}'
# tRes_l = list(inp_FltAVali_fefi(f' по очереди по одной любые цифры {tResLLen_co} раза',
#     laInPValues_co=tResLLen_co, laValiInPMsg_s=f'a Integer OneOf{tValiV_t}',
#     laVali_cll=lambda x: x in tValiV_t))
# tValiV_t = ('Y', 'N')
# tRes_l = list(inp_FltAVali_fefi(f' Ts 2 times',
#     laInPValues_co=2, laInPTypeFlt_cll=None, laDfV_s='Y',
#     laAcceptEmptyInPAsDf_b=True, laValiInPMsg_s=f'a character OneOf{tValiV_t}',
#     laVali_cll=lambda _s: _s.upper() in tValiV_t))
# tRes_l.sort()
# print(tRes_l)

@dataclass
class Menu_c():

  fMenuItm_d: dict = field(default_factory=dict)
  fInnStt_d: dict = None
  fPrnInnStt_cll: Callable = None # [self, dict, file]; ??Df: IF fInnStt_d is !None -> print(fInnStt_d)
  fIterSortKey_cll: Callable = None # [key] ??(Prop4Set): AsIn2fMenuItm_d OR (lambda _el: str(_el))|int
  fHeaFmt_s: str = None
  fFooFmt_s: str = None
  fItmFmt_s: str = '{_k!s:>2}. {_v[0]}'
  fAddHst_b: bool = True
  fFile_o: object = sys.stdout

  def __post_init__(self):
    self.fMenuItm_d = dict(self.fMenuItm_d)
    if self.fInnStt_d is not None:
      self.fInnStt_d = copy.deepcopy(dict(self.fInnStt_d))
      if self.fPrnInnStt_cll is None:
        self.fPrnInnStt_cll = lambda sf_o, lafInnStt_d, file=self.fFile_o: print(lafInnStt_d, file=file)
    if self.fHeaFmt_s is not None: self.fHeaFmt_s = str(self.fHeaFmt_s)
    else: self.fHeaFmt_s = glSep_s
    if self.fFooFmt_s is not None: self.fFooFmt_s = str(self.fFooFmt_s)
    else: self.fFooFmt_s = glSep_s[:len(glSep_s)//3 *2]
    
    self.fRunLoop_b = bool(self.fMenuItm_d)
    if self.fAddHst_b:
      if self.fInnStt_d is None:
        self.fInnStt_d = {'kActHst_l':[]}
      if 'kActHst_l' not in self.fInnStt_d:
        self.fInnStt_d['kActHst_l'] = []
      self.fActHst_l = self.fInnStt_d['kActHst_l']
      self.fActHst_l.append((time.time_ns(), 'Inn', '__post_init__', True))
    else:
      self.fActHst_l = None

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

  # 2Do: MaB: oup_fmp(self, file=fFile_o)
  # 2Do: MaB Onl(9+KeyExit OR Fit2Scr+KeyExit) w/Set(sf.WhiVieItmKey_l)
  def prn_fmp(self, file=fFile_o):
    if bool(self.fMenuItm_d):
      if self.fHeaFmt_s != '': print(self.fHeaFmt_s, file=file)
      print(*(self.fItmFmt_s.format(_k=_k, _v=self[_k]) for _k in self),
          sep='\n', file=file)
      self.prn_Info_fmp(file=file)
      if self.fFooFmt_s != '': print(self.fFooFmt_s, file=file)

  # def __str__(self):; __format__; tVieHst_fmp
  def prn_Info_fmp(self, file=fFile_o):
    if self.fPrnInnStt_cll and callable(self.fPrnInnStt_cll):
      self.fPrnInnStt_cll(self, laInnStt_d=self.fInnStt_d, file=file)

  # def add_Itms?_ffm(self):
  # def del_Itms?_ffpm(self):
  # def get_Keys?_ffpm(self):

  # def run_ffpm(self):
  def __call__(self, file=fFile_o): # MainLoop
    if self.fActHst_l is not None:
      self.fActHst_l.append((time.time_ns(), 'Inn', 'Beg:MainLoop', True))
    while self.fRunLoop_b:
      self.prn_fmp(file=file)
      li_s = inp_FltAVali_fefi(f' пункт меню', laInPTypeFlt_cll=None,
          file=file)[0].strip()
      if li_s in self:
        li_k = li_s
      else:
        try: li_k = int(li_s)
        except ValueError as le_o: li_k = None
        else:
          if li_k not in self: li_k = None
      if li_k is not None:
        lo_cll = self[li_k][1]
        if lo_cll is None: # 2Do:AddHst
          print(f'DVL: None 4 calling Fu() пункт меню({li_k})', file=file)
          continue
        else:
          loRes_a = lo_cll(self, file=file) # 2Do:AddHst
          if self.fActHst_l is not None:
            self.fActHst_l.append((time.time_ns(), 'InP',
                f'({li_s})' + self[li_k][0], loRes_a))
      else:
          print(f'Неверный пункт меню({li_s})', file=file) # 2Do:AddHst
    else: # 2Do:AddHst
      if self.fHeaFmt_s != '': print(self.fHeaFmt_s, file=file)
      print('До свидания!', file=file)
      if self.fActHst_l is not None:
        self.fActHst_l.append((time.time_ns(), 'Inn', 'End:MainLoop', True))
      if self.fFooFmt_s != '': print(self.fFooFmt_s, file=file)

    return self.fInnStt_d # 2Do:RetHst

