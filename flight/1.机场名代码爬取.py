import requests
import pandas as pd

headers = {

    'Connection': 'keep-alive',
    'Cookie': 'PHPSESSID=os2lbagdh5virpt0r90t78uei1; Hm_lvt_de76267abe273488e66f73620a0a2118=1567647865; _ga=GA1.2.740261823.1567647866; _gid=GA1.2.387000010.1567647866; Hm_lpvt_de76267abe273488e66f73620a0a2118=1567666299; _gat_gtag_UA_93103382_2=1',
    'Host': 'data.variflight.com',
    'Referer': 'https://data.variflight.com/profiles/Airports',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
            }
url = 'https://data.variflight.com/analytics/codeapi/initialList'
r = requests.get(url=url,headers=headers)
r= r.json()
# print(r.json())
data_ = r['data']
id = []
ICAO = []
en = []
fn = []
id = []
initial = []
text = []

A_ = data_['A']
B_ = data_['B']
C_ = data_['C']
D_ = data_['D']
E_ = data_['E']
F_ = data_['F']
G_ = data_['G']
H_ = data_['H']
I_ = data_['I']
J_ = data_['J']
K_ = data_['K']
L_ = data_['L']
M_ = data_['M']
N_ = data_['N']
O_ = data_['O']
P_ = data_['P']
Q_ = data_['Q']
R_ = data_['R']
S_ = data_['S']
T_ = data_['T']
U_ = data_['U']
V_ = data_['V']
W_ = data_['W']
X_ = data_['X']
Y_ = data_['Y']
Z_ = data_['Z']

for index in range(len(A_)):
    id_ = A_[index]['id']
    id.append(id_)
    ICAO_ = A_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = A_[index]['en']
    en.append(en_)
    fn_ = A_[index]['fn']
    fn.append(fn_)
    initial_ = A_[index]['initial']
    initial.append(initial_)
    text_ = A_[index]['text']
    text.append(text_)
for index in range(len(B_)):
    id_ = B_[index]['id']
    id.append(id_)
    ICAO_ = B_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = B_[index]['en']
    en.append(en_)
    fn_ = B_[index]['fn']
    fn.append(fn_)
    initial_ = B_[index]['initial']
    initial.append(initial_)
    text_ = B_[index]['text']
    text.append(text_)

for index in range(len(C_)):
    id_ = C_[index]['id']
    id.append(id_)
    ICAO_ = C_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = C_[index]['en']
    en.append(en_)
    fn_ = C_[index]['fn']
    fn.append(fn_)
    initial_ = C_[index]['initial']
    initial.append(initial_)
    text_ = C_[index]['text']
    text.append(text_)



for index in range(len(D_)):
    id_ = D_[index]['id']
    id.append(id_)
    ICAO_ = D_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = D_[index]['en']
    en.append(en_)
    fn_ = D_[index]['fn']
    fn.append(fn_)
    initial_ = D_[index]['initial']
    initial.append(initial_)
    text_ = D_[index]['text']
    text.append(text_)

for index in range(len(E_)):
    id_ = E_[index]['id']
    id.append(id_)
    ICAO_ = E_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = E_[index]['en']
    en.append(en_)
    fn_ = E_[index]['fn']
    fn.append(fn_)
    initial_ = E_[index]['initial']
    initial.append(initial_)
    text_ = E_[index]['text']
    text.append(text_)

for index in range(len(F_)):
    id_ = F_[index]['id']
    id.append(id_)
    ICAO_ = F_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = F_[index]['en']
    en.append(en_)
    fn_ = F_[index]['fn']
    fn.append(fn_)
    initial_ = F_[index]['initial']
    initial.append(initial_)
    text_ = F_[index]['text']
    text.append(text_)

for index in range(len(G_)):
    id_ = G_[index]['id']
    id.append(id_)
    ICAO_ = G_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = G_[index]['en']
    en.append(en_)
    fn_ = G_[index]['fn']
    fn.append(fn_)
    initial_ = G_[index]['initial']
    initial.append(initial_)
    text_ = G_[index]['text']
    text.append(text_)

for index in range(len(H_)):
    id_ = H_[index]['id']
    id.append(id_)
    ICAO_ = H_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = H_[index]['en']
    en.append(en_)
    fn_ = H_[index]['fn']
    fn.append(fn_)
    initial_ = H_[index]['initial']
    initial.append(initial_)
    text_ = H_[index]['text']
    text.append(text_)

for index in range(len(I_)):
    id_ = I_[index]['id']
    id.append(id_)
    ICAO_ = I_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = I_[index]['en']
    en.append(en_)
    fn_ = I_[index]['fn']
    fn.append(fn_)
    initial_ = I_[index]['initial']
    initial.append(initial_)
    text_ = I_[index]['text']
    text.append(text_)

for index in range(len(J_)):
    id_ = J_[index]['id']
    id.append(id_)
    ICAO_ = J_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = J_[index]['en']
    en.append(en_)
    fn_ = J_[index]['fn']
    fn.append(fn_)
    initial_ = J_[index]['initial']
    initial.append(initial_)
    text_ = J_[index]['text']
    text.append(text_)

for index in range(len(K_)):
    id_ = K_[index]['id']
    id.append(id_)
    ICAO_ = K_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = K_[index]['en']
    en.append(en_)
    fn_ = K_[index]['fn']
    fn.append(fn_)
    initial_ = K_[index]['initial']
    initial.append(initial_)
    text_ = K_[index]['text']
    text.append(text_)

for index in range(len(L_)):
    id_ = L_[index]['id']
    id.append(id_)
    ICAO_ = L_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = L_[index]['en']
    en.append(en_)
    fn_ = L_[index]['fn']
    fn.append(fn_)
    initial_ = L_[index]['initial']
    initial.append(initial_)
    text_ = L_[index]['text']
    text.append(text_)

for index in range(len(M_)):
    id_ = M_[index]['id']
    id.append(id_)
    ICAO_ = M_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = M_[index]['en']
    en.append(en_)
    fn_ = M_[index]['fn']
    fn.append(fn_)
    initial_ = M_[index]['initial']
    initial.append(initial_)
    text_ = M_[index]['text']
    text.append(text_)

for index in range(len(N_)):
    id_ = N_[index]['id']
    id.append(id_)
    ICAO_ = N_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = N_[index]['en']
    en.append(en_)
    fn_ = N_[index]['fn']
    fn.append(fn_)
    initial_ = N_[index]['initial']
    initial.append(initial_)
    text_ = N_[index]['text']
    text.append(text_)

for index in range(len(O_)):
    id_ = O_[index]['id']
    id.append(id_)
    ICAO_ = O_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = O_[index]['en']
    en.append(en_)
    fn_ = O_[index]['fn']
    fn.append(fn_)
    initial_ = O_[index]['initial']
    initial.append(initial_)
    text_ = O_[index]['text']
    text.append(text_)

for index in range(len(P_)):
    id_ = P_[index]['id']
    id.append(id_)
    ICAO_ = P_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = P_[index]['en']
    en.append(en_)
    fn_ = P_[index]['fn']
    fn.append(fn_)
    initial_ = P_[index]['initial']
    initial.append(initial_)
    text_ = P_[index]['text']
    text.append(text_)

for index in range(len(Q_)):
    id_ = Q_[index]['id']
    id.append(id_)
    ICAO_ = Q_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = Q_[index]['en']
    en.append(en_)
    fn_ = Q_[index]['fn']
    fn.append(fn_)
    initial_ = Q_[index]['initial']
    initial.append(initial_)
    text_ = Q_[index]['text']
    text.append(text_)

for index in range(len(R_)):
    id_ = R_[index]['id']
    id.append(id_)
    ICAO_ = R_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = R_[index]['en']
    en.append(en_)
    fn_ = R_[index]['fn']
    fn.append(fn_)
    initial_ = R_[index]['initial']
    initial.append(initial_)
    text_ = R_[index]['text']
    text.append(text_)

for index in range(len(S_)):
    id_ = S_[index]['id']
    id.append(id_)
    ICAO_ = S_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = S_[index]['en']
    en.append(en_)
    fn_ = S_[index]['fn']
    fn.append(fn_)
    initial_ = S_[index]['initial']
    initial.append(initial_)
    text_ = S_[index]['text']
    text.append(text_)

for index in range(len(T_)):
    id_ = T_[index]['id']
    id.append(id_)
    ICAO_ = T_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = T_[index]['en']
    en.append(en_)
    fn_ = T_[index]['fn']
    fn.append(fn_)
    initial_ = T_[index]['initial']
    initial.append(initial_)
    text_ = T_[index]['text']
    text.append(text_)

for index in range(len(U_)):
    id_ = U_[index]['id']
    id.append(id_)
    ICAO_ = U_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = U_[index]['en']
    en.append(en_)
    fn_ = U_[index]['fn']
    fn.append(fn_)
    initial_ = U_[index]['initial']
    initial.append(initial_)
    text_ = U_[index]['text']
    text.append(text_)

for index in range(len(V_)):
    id_ = V_[index]['id']
    id.append(id_)
    ICAO_ = V_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = V_[index]['en']
    en.append(en_)
    fn_ = V_[index]['fn']
    fn.append(fn_)
    initial_ = V_[index]['initial']
    initial.append(initial_)
    text_ = V_[index]['text']
    text.append(text_)

for index in range(len(W_)):
    id_ = W_[index]['id']
    id.append(id_)
    ICAO_ = W_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = W_[index]['en']
    en.append(en_)
    fn_ = W_[index]['fn']
    fn.append(fn_)
    initial_ = W_[index]['initial']
    initial.append(initial_)
    text_ = W_[index]['text']
    text.append(text_)

for index in range(len(X_)):
    id_ = X_[index]['id']
    id.append(id_)
    ICAO_ = X_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = X_[index]['en']
    en.append(en_)
    fn_ = X_[index]['fn']
    fn.append(fn_)
    initial_ = X_[index]['initial']
    initial.append(initial_)
    text_ = X_[index]['text']
    text.append(text_)

for index in range(len(Y_)):
    id_ = Y_[index]['id']
    id.append(id_)
    ICAO_ = Y_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = Y_[index]['en']
    en.append(en_)
    fn_ = Y_[index]['fn']
    fn.append(fn_)
    initial_ = Y_[index]['initial']
    initial.append(initial_)
    text_ = Y_[index]['text']
    text.append(text_)

for index in range(len(Z_)):
    id_ = Z_[index]['id']
    id.append(id_)
    ICAO_ = Z_[index]['ICAO']
    ICAO.append(ICAO_)
    en_ = Z_[index]['en']
    en.append(en_)
    fn_ = Z_[index]['fn']
    fn.append(fn_)
    initial_ = Z_[index]['initial']
    initial.append(initial_)
    text_ = Z_[index]['text']
    text.append(text_)


df = pd.DataFrame({'id':id,'ICAO':ICAO,'en':en,'fn':fn,'initial':initial,'text':text})
mingzi = '机场代码'
df.to_csv(r'D:\!!python result\Varifight\{}.csv'.format(mingzi),mode='a',index = 0)
print(df.head(2))