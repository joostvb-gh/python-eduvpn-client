mock_config = """# OpenVPN Client Configuration
dev tun
client
nobind
remote-cert-tls server
comp-lzo
verb 3
server-poll-timeout 10
auth SHA256
cipher AES-256-CBC
tls-version-min 1.2
tls-cipher TLS-ECDHE-RSA-WITH-AES-256-GCM-SHA384
<ca>
-----BEGIN CERTIFICATE-----
MIIFJDCCAwygAwIBAgIJAJ1NwjmG+n/3MA0GCSqGSIb3DQEBCwUAMBExDzANBgNV
BgNVBAMTBlZQTiBDQTCCAiIwDQYJKoZIhvcNAQEBBQADggIPADCCAgoCggIBALOW
Zak2nNf7uZ1+XaoR78gkBHqszXlaFdPByC2bQn0vrsGurUHTXO843MDfsckbeNEE
8ZrqXnNnqaojP90UkGIXbXLl7U8kborvKF/gQm6gsk3O0obhTVDdEj3kYKFGxmqu
QHJo3C2amro4wVIv/BhXzIv6oP11Va/6FcwAYj8disNcxJgXWSUdARrEIC3PME58
Ld+a2jvXL/m8xBp+qVThvfmq2Pak1olhbgDueUSsQYiQZMq2rX3/1f+SInxZt3kJ
BAMTBlZQTiBDQTAeFw0xNzAyMjcxNDA5NTJaFw0yMjAyMjcxNDA5NTJaMBExDzAN
0LWOOSBzGwYnjfGmm/JzM06jHq+vyfrFwl28uNuCVRwJpvmjJC8+O8TYFgOrx8Oe
Q7gbC+Wrx1Nv/u2j59ofTPk2R5oNdrYt3h5YVv0WocHmiYb+CzdwxBvyZ50Uy1+x
0XEZpfYV4x6m1/8sEqYANx+5U+3KXZznUXlevyLqgS5tn3hGuxwRuxb5AifwRRmF
z5wSVuDilCGnzNGyqJvP4rKAlGakQx8nyFIsdMsa7OpQVd4n+ex5HhfMlSa7Bvpj
DK+8p3ynd11jihCkFAzOqldBN2hR1gCjx2b52zLk0vzTyyiCEebqb9hqKf+jb3/j
FyE9gzlm2uR9rvvyVKnsDnuCb5vsnWdPTUvBov6tAgMBAAGjfzB9MB0GA1UdDgQW
BBTmp4VYXwUkBWl7cK4WspgpaIyI8zBBBgNVHSMEOjA4gBTmp4VYXwUkBWl7cK4W
8CKV1gYtjPBc6OOMNYyXfXlu0qtkLljV/Pdt4hxUNyyptPvJgP8xLg+z+RoZZmxV
spgpaIyI86EVpBMwETEPMA0GA1UEAxMGVlBOIENBggkAnU3COYb6f/cwDAYDVR0T
bifEWHPpbS1RceRBzk+QUNjRmQrT+hCdzpHro8SdbaPg7eRG7HvC5zi6tvxLirn/
0ThsnRb5xWkDYQ2BXponBTnFRyYaiaXyEuJTAvfbF51R3ycy03tl4v15UtzW/Spa
n1CqNVHH+vinqSo1cXV17b9PFcfohA2n86tDwkqOC+0fPX3KO2v8ALANxNYEunzW
xWPQM0wTgoXuUpOx8/UkGYVxOnwy9uHtL4HS1+5tyTjKv5Ld8NktDPiNvSHTV8zt
BAUwAwEB/zALBgNVHQ8EBAMCAQYwDQYJKoZIhvcNAQELBQADggIBACIReoZBwxA+
S5sb3PokhBktJxEy8MzamAwuJEpiLikYPUJvoNI1XzH9JJR6cI1rfGtABb8GCikA
9KxDmz8SBuJVjYuWA/d0DlLAAhUiq+gIkuh1YaC6dhjUxhQAxMe/WW38KHV9BlrR
WrnstYLLSuVkwLmg5h+ltra2rqqyRTYX66+eKF8gj4p/xP0JAiAsBSLKztuSodce
rhYC3Jy9EQ0MBP0oujwdOLSLMoGqM4xZPiMmsELgOVoeX5ypk2DPpWwNeOYVsDrV
b2VJ/qPt0tfQjGIEYba34wNAsmuI/WLjayKVHz6zwG1nueG+9/JHVW1lYOv3iwXe
PRTJkpeEl44pu4vsvU/XyAoUijFwwuazzbqLTNwc7h7kM7Vq/beCyN3HkyW44sla
nIYUto+cPuPcEEuvyVeOT6UjzKgnLbmY
-----END CERTIFICATE-----
</ca>
key-direction 1
<tls-auth>
#
# 2048 bit OpenVPN static key
#
-----BEGIN OpenVPN Static key V1-----
bbb4a1bc4e97ce6cfa7ea930c3bb7feb
e1af60b6b06a6acd39c38c29d6c0197c
85dab27a52c30d0e31b4ce80bfb61dab
69577c09b349787b7e9336a7e655a5bc
51c3ef467fdf867a1cc951ae6ebd995a
ba096690d73fbd8cd41ffff231c1c17e
ef022cedf84639dc04b8fb204066f31e
484804c5535d50c428794a68ba65b432
781c4e76285ba799cbd81bb4473b3f45
d7b127ab548377645dd82c14fd5db3b2
8487de31db848a1a476616ab4650a55c
e1a42d4a8521218ac56789e3c10848e7
8349bea907fcbc333282879306cee469
b0b85a410294cdea5eb29ae009f98687
8cb2f25feff977b15b3249bee779659c
367e7c0aa4d23d8af9d948f992fbd10a
-----END OpenVPN Static key V1-----
</tls-auth>
remote internet.demo.eduvpn.nl 1194 udp
remote internet.demo.eduvpn.nl 1194 tcp
remote internet.demo.eduvpn.nl 443 tcp
<cert>
-----BEGIN CERTIFICATE-----
MIIFSzCCAzOgAwIBAgICAdkwDQYJKoZIhvcNAQELBQAwETEPMA0GA1UEAxMGVlBO
IENBMB4XDTE3MDgyNDE0MDk0NloXDTE4MDgyNDE0MDk0NlowKzEpMCcGA1UEAxMg
ZDU1MDhmMjk3MjRmZTc4MTEyZTViZGY1MmZjOWUwMTYwggIiMA0GCSqGSIb3DQEB
AQUAA4ICDwAwggIKAoICAQCZ5/FNshijQG51CVpyXdYpk6gnQbEX9ZKTW5S2HULB
Z0jmVOisdW6eV8nHTCkpZx8MWRvIe7OvndBms4I8/31s30sQM3UzLpQqUelS6DvG
hNT5I9AYzrISOFkuZ0zUIRQYTkHNEBzYxkEqYqMvOMecY48CQ5CX6PY8TI390ge4
kzdllrHjr8c8LjnmHa3uHwruRrzFFtnQFHqCbr9hBaDEK8ShVLmHdHvpY43aGEec
bqCzPwemp8+NW9Ibv+iocj4ISJfMKSHAhV8PogIYT0mNyp1O3OMV8XEib1/lEj7r
EJsAcnnNjL/iY6fqNNcxHC0az0GPkuymiHEh5p17/wgBrHgtN6ukAIskUbhcSh7c
63qy5n3xJvpu6x9YF57rXl6eRG9ybVYu4SjJRVQnBcK56KTrJ9kJk3j7W5YWxOSf
fJ1KyFQtp0XKS4QndE5rvu+pEXvUAGJFZ31N1ZmAQzrUINUNLz89vuuBYE5Nxtk5
HQFmEqZ934EtvcHRl719fl0Dd7QnT6f2Ph9/TxX8K7yye1wKwFcPlTVoJs+8/Rlo
ssjbwMDY+dpSrtMRSj9VaEkJNKqNhKFAOshvaru3eeWjr4yBu762r1Npw0iczRED
9DLJM7j1zsEEGVYyIqA2MAK91FYraMT1jjKG1mox1Vm+CElWY72coNN7+a+e7f/5
/dMl6s08MEEGA1UdIwQ6MDiAFOanhVhfBSQFaXtwrhaymClojIjzoRWkEzARMQ8w
0wIDAQABo4GSMIGPMAkGA1UdEwQCMAAwHQYDVR0OBBYEFOHZWTq3OVB886F023oQ
BgNVHQ8EBAMCB4AwDQYJKoZIhvcNAQELBQADggIBAKEajJgeStmXI7B2KeSNDBVt
DQYDVQQDEwZWUE4gQ0GCCQCdTcI5hvp/9zATBgNVHSUEDDAKBggrBgEFBQcDAjAL
NYm1JwJwegYk6PeiDIvLYl4FrUznNYHT3udOd9ikn/vFRCEexPTksasNpka+tRme
PH82cZtwHZZgajpUa640vQXW7nmZC6YdTkZW74he1Zqi28FNMNAQ7dzrDzMdVOyv
NSbQQTX0Qf6Yobocb8jmHivonAR7dZ1MzGPyf6w7OqkQ+7mszOX0o2IZFsAws3L0
PCzqUP9LwZCk+gtA5mmaaXXqMMhoL9/QjFNJBtxllz9ksMyCnfQDRTZECjNsODH4
JcBcJPTWQ1c67XJNDXaJ3QMRlJRqdHAGJxg1Si4ajsoHD6fVqpKvCwyhIFSGMQhW
eN4i+8OTrr94YcLpBrP4oK1zTYfUdDDk/SP6Ax+xJEIYbLmJR5jci9di0Kdc4FJL
fMmH62tFb/U7nYEwT3V9+IXFD6eljaK8k2E1VISzPV/mT5RkmBGzx/MB4NHUX35U
T93kKrIIM0/VXzaMOr2iVTuc90im5yFczFXuy0JhL1agV7yCEW43YUClGESg48W6
3rp1ufZWraHITnyUPcHObgq8/51uKHkPIpNx1F4rqrXlrgZJfjANVO3MLJkxvdRA
zxWzRatGON7I9fPr4zd9h6au5rN9iOObof+JZGPk9tbH2Bg6wV3qZNIPZPVUBfc4
q5QpoF0ATpXqjhwu4yI9
-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN PRIVATE KEY-----
MIIJQgIBADANBgkqhkiG9w0BAQEFAASCCSwwggkoAgEAAoICAQCZ5/FNshijQG51
CVpyXdYpk6gnQbEX9ZKTW5S2HULBZ0jmVOisdW6eV8nHTCkpZx8MWRvIe7OvndBm
YqMvOMecY48CQ5CX6PY8TI390ge4kzdllrHjr8c8LjnmHa3uHwruRrzFFtnQFHqC
s4I8/31s30sQM3UzLpQqUelS6DvGhNT5I9AYzrISOFkuZ0zUIRQYTkHNEBzYxkEq
ogIYT0mNyp1O3OMV8XEib1/lEj7r63qy5n3xJvpu6x9YF57rXl6eRG9ybVYu4SjJ
RVQnBcK56KTrJ9kJk3j7W5YWxOSfEJsAcnnNjL/iY6fqNNcxHC0az0GPkuymiHEh
br9hBaDEK8ShVLmHdHvpY43aGEecbqCzPwemp8+NW9Ibv+iocj4ISJfMKSHAhV8P
1ZmAQzrUINUNLz89vuuBYE5Nxtk5ssjbwMDY+dpSrtMRSj9VaEkJNKqNhKFAOshv
aru3eeWjr4yBu762r1Npw0iczREDHQFmEqZ934EtvcHRl719fl0Dd7QnT6f2Ph9/
5p17/wgBrHgtN6ukAIskUbhcSh7cfJ1KyFQtp0XKS4QndE5rvu+pEXvUAGJFZ31N
TxX8K7yye1wKwFcPlTVoJs+8/Rlo9DLJM7j1zsEEGVYyIqA2MAK91FYraMT1jjKG
nR61YDAkrRKaBC9mH1CtuS0godFwHL6nGbjegnMJmGCJEdpvFr6OlXRIaWFDm6R2
VBHBKWbf4xMEGdiVPiWVaUSRe0NmA0cEfszCPrNiB7qZyExrD1VYZMzF8wCgRy9M
1mox1Vm+CElWY72coNN7+a+e7f/50wIDAQABAoICABeu9pYTMvFkR9sgvlddE0jA
rsQVa5nE0qeCzFLj0CZaGSs73lIASbN8FZLQvGQpSMBUCFZ35rq7fAK4UiD3Ab9O
ceqh2RwWVGeNJf+VKDObv/zptTW33s/UxLUEpYLouby3IUNFif6azXDzhzieDVHb
XoDnAnozouJ44i5vHglHsHwzTz4N6OLVf9/fMdZgBmt5YnR0E+Tx/nH6uavdaql0
UOrWo9oxVaQbmseV9uceqwIKT/4YUrsZByMYDBBnzB3wNdPH/Jaor3EzaAkfolz8
7UOHN+Cxy7A/BBltS3xITG9XzBhN50BUNLXy/+zYCHn4Sm8uqmoFgkbxECLvhglE
HMO7HVRlDKAJEKUvRKDNQd/N3GnGLnAuLUrSapW2bKizTEDMPsGV/1dyjDxNbbMF
JaP675WsSDtN2Rozyh6xmBB0vBjzqEaC88CidVjU6frXbFZ3W1s67sM4oGhPyE2D
U6QZsnEslPfjyKzcxqxvMobYphW9kS1He32Z0efR8E/UTvMbfUUqB2u+Jue9RAFy
XK9Ep8sqIdDK77R5K/BRAoIBAQDJ/HjrhIWwwZ8IzlB5qc+aqA2kTY11apoJRXAN
UOvHx77JYEvTuwbvXUqZVTxzne7jwCOW81JitGXOifLAx3sFW3VM9mSfzt0Ib6Ke
B9csNtzWlvAD7X9nWnxZBGpBSCILxag2iwYxSEA20x/dORO6VsDzXWhc2MucYiQt
enp60dBJEVynpCQ3YsKrfSss9raY8LTS9AKz2kpWpj4T1U2u8B7SQU0OUN/v6pck
5svkeSPkfrvC8XUb+nleabpGXdttt0MXEG5wqzWkt/xFX1oNjPak1T3ENlNPw/hQ
EGY/PSlt6c48Kj9Wyowr8omzHMLdM2J8iKLwFB9RSQhFtmkpAoIBAQDDEAHLvc25
uLZujCehUfy9lZrg7WGbvfM6RWWL3Z8JbKfU51R21hX7vBa/TE/NDL5kOfzt2mED
+d5zUSU/mg2GLy6tvqqUz7V//Oc9bVeakrmW8WMBnn1y0997wUFJRhcmX5CyLmWF
t/EUswcRHP/MneOA/livQmC8zodGJMYjWZv+5H2yEdxQLPF05MV52cX/oUy1Hn+q
6YaqeKEck0TbZvgVqMq2nSeAp3bLrRbWtKyylZbinPFBU26I2ZnLA877z+eeP/qu
5P0dwFpcUxipycJZOpe5oRpokdG3qgBd9ER69GAgZibJxZeh0iC0O5PWbJ+4bBbO
F4oxDDgX8lcQ5eH2KRn7k2JWH5P9llEG47e31k3N8q1TLASzcIZZGujYixAxBY2U
Q5r3tDMaOx/dnaJSsxL6ohGQVYiFukb/0NQ+CMx4fSdzAwygvSu0Blakk7jwSDcj
TWapR+xXPj7/IUcWshZDN9Ov9Bkx19y6wQtJGvdGLLgnQdlnpaGgHfVnltG5OGGu
2ozk53QwT56bAoIBADTEaU6V21s26fYh9/Igw6SSnKW8wOTYyY78fe6TydZRM2hB
UHdXMULq4RJt67aeaUuBLqwhpQcZUuxaF8OUqOu3vUWOW7QOusHxljSMuDlzH/yf
Xs493ecq8xSdaNy46/HisVbXvZxL5Wf0yz52zK8+Lqbqm7KoI3UEFxpSVEkzdIKK
dCkbHmE6CW/aar0z2c+eW0Z8J1MvcyQB/eNjEn/uLBrITUqCr+8gu3WajWRlbexf
F8F4wEw6jX+f52fUVYXBzVGyY5D8RA9FlJAg2wei4ouusF1qW9cqY2mvUU7h50Q9
5Qngu5VP6ticTw7kx5+ECgmgpHh1uUzB+JBFvCkCggEAT8jeUy2hVhNsomDPxSot
Z9hoJMPTlnoVTEQzDQARVWS1Np6FBs/WxjeQAJ2wkB9QrCLPxCS7LoovFdo1m4nJ
jrkdq02R/bVtjdQHCa6ZU9Szpe8K2nWt693MNb4y7kVoJM5tTgu4EIfIFWCuX4xR
XZzDZH7KJ+xm7r21Go6K9fqEg+gwvajcsjYhFfxQbsCjh1rDYZzE7lhcA055Q2Mv
ovWp2Nq55ZvSvrzoZCJWEU3BZVBA/Hu6GTA9EE5REaML+PaaD/ar/lNQGKXk4D5p
W6t0CpKalc30qZHSQfQBREDivbQGMy1rBtxhFc8ru9zkB+QagoQyIBkX/8CBrDbv
fQKCAQEAjOoIfVWm4t4wps72SIDZSugmfD2M4dPTAKyshQeTugkhCZ2pCBuoTmSW
SdooJUoYqqMaG2Yf63D4C8oTRIAqqPxsI+p3SSd6P4YnSN69fcmQ8qAy/RJQ0Mn5
xL2Pccm97PHvBS/J8JMzBn8y3hhT0g==
-----END PRIVATE KEY-----
</key>
"""
