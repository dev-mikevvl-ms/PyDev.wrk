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

glScrWid_s = 70
glSep_s = '_' *glScrWid_s

def inp_FltAVali_fefi(laWhatInPMsg_s, laInPValues_co=1, laValiInPMsg_s='',
    laVali_cll=None, laInPTypeFlt_cll=int, laMaxInPTry_co=11,
    laAcceptEmptyInPAsDf_b=False, laDfV_s=None, laVerbose_i=None) -> tuple:
  if laInPValues_co < 1: raise ValueError(f'laInPValues_co must be > 0, now:{laInPValues_co}')
  loTypeAValiFlsCo_l, loRes_l, loMaxTry_co = [0, 0], [], int(max(laInPValues_co, laMaxInPTry_co))
  if laValiInPMsg_s and laVali_cll:
    lo_s = f' - your value will be validated as({laValiInPMsg_s}'
    if lo_s[-1] == '\n': lo_s = lo_s[:-1] + ')\n -'
    else: lo_s += ') -'
  else: lo_s = ''
  lo_s = f"Please, Input{laWhatInPMsg_s}{lo_s} and press Enter"
  if laAcceptEmptyInPAsDf_b and laDfV_s is not None:
    lo_s += f"(on default '{laDfV_s}')"
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
          f'- Exception:{type(leExc_o).__name__}({leExc_o}) raised.')
    else:
      if laVali_cll is not None:
        if laVali_cll(liChe_i):
          loRes_l.append(liChe_i)
          print(f"\tMSG: You input:'{liChe_i}' valid.")
        else:
          loTypeAValiFlsCo_l[1] +=1
          lo_s = f' because of NOT {laValiInPMsg_s}' if laValiInPMsg_s else ''
          print(f"\tERR: You input:'{liChe_i}' INVALID{lo_s}.")
      else:
        loRes_l.append(liChe_i)
        print(f"\tMSG: You input:'{liChe_i}'.")
        # if liChe_i == tPtt_i: tOk_co +=1
    # print(f'DBG: {loRes_l=}')
    if len(loRes_l) == laInPValues_co: break  
    if laMaxInPTry_co:
      if l_co == int(loMaxTry_co -1):
        if loRes_l:
          print(f"\tWRN: Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co}, return {tuple(loRes_l)} as User input.")
        else:
          raise ValueError(f'Rich max(laInPValues_co, laMaxInPTry_co):{loMaxTry_co} but loRes_l is Empty - nothing return as User input.')
      else:
        lo_s = '' if l_co == (loMaxTry_co -2) else 's'
        lo_s = f' and {loMaxTry_co - l_co -1} attempt{lo_s} left'
    else: lo_s = ''
    print(f'MSG: It remains to input {laInPValues_co - len(loRes_l)} more value{lo_s}.')
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
