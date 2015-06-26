def ex_gcd(x, y):
	# Extended Euclidean algorithm
	# a*x + b*y = v
	u, v = x, y
	a,b, c,d = 0,1, 1,0
	while u != 0:
		q, r = (v // u), (v % u)
		m, n = (a - c * q), (b - d * q)
		v,u, a,b, c,d = u,r, c,d, m,n
	return a, b, v

def mod_inv(x, y):
	# modular multiplicative inverse
	# a*x == 1 mod y
	a, b, g = ex_gcd(x, y)
	if g != 1:
		return None
	else:
		return a % y

def phi(p, q):
	# Euler's totient function
	return (p - 1) * (q - 1)

if __name__ == '__main__':
	msg = "hogehoge"

	# prime numbers
	p = """00:d9:77:da:d9:33:b8:b5:b3:65:8b:72:17:4f:d0:
	06:de:46:34:19:11:d9:0c:8a:96:03:97:0e:c7:ec:
	73:85:2a:b2:b9:ba:37:12:6c:c2:c1:fa:66:f6:03:
	82:03:83:73:1a:88:33:de:a8:74:03:7e:fe:d4:5f:
	ce:92:fc:2a:a0:09:45:3a:b5:d8:ad:62:53:01:86:
	33:ec:39:aa:48:2b:81:6d:c0:83:f2:ee:26:c4:12:
	2e:3a:d6:12:cf:25:ac:40:18:f8:5d:d0:86:62:c8:
	aa:63:ac:7a:40:ea:b9:74:1a:96:0b:a8:59:1d:e4:
	ad:1a:6c:c0:08:2e:11:26:d5"""

	q = """00:cf:19:7d:0a:06:98:f9:a7:17:27:14:7c:67:51:
	d8:2e:19:4c:11:29:61:94:01:ce:79:6d:a4:b0:93:
	91:d7:30:b1:c6:24:d2:cf:b5:62:cd:fe:31:38:91:
	2a:06:c2:c7:dc:8f:3c:f3:59:e1:1b:e1:e2:e3:a0:
	3e:5e:f0:a3:00:a5:2b:1f:f6:e4:c1:55:d7:3b:5c:
	00:e2:51:e9:14:72:cb:72:14:25:dd:3a:86:8c:50:
	72:ed:ac:c2:cf:04:55:1d:05:90:ff:f6:59:bd:aa:
	86:28:f0:74:0c:6a:27:dd:f9:6d:bd:b0:77:80:34:
	d6:dc:e4:4c:9e:e1:dd:6e:db"""

	# string -> hex -> int
	msg = int(msg.encode('hex'), 16)
	p = int(p.replace('\n', '').replace('\t', '').replace(':', ''), 16)
	q = int(q.replace('\n', '').replace('\t', '').replace(':', ''), 16)

	# public key
	mod = p * q
	public_exp = 65537 # =0x10001

	# secret key
	private_exp = mod_inv(public_exp, phi(p,q))

	#encrypt
	encrypted_msg = pow(msg, public_exp, mod)

	#decrypt
	decrypted_msg = pow(encrypted_msg, private_exp, mod)

	print "Original Massage: %s \n" % hex(msg).replace('0x', '').decode('hex')
	print "Modulus: %s \n" % mod
	print "Public Exponent: %s \n" % public_exp
	print "Prime 1: %s \n" % p
	print "Prime 2: %s \n" % q
	print "Private Exponent: %s \n" % private_exp
	print "Encrypted Massage: %s \n" % encrypted_msg
	print "Decrypted Massage: %s \n" % hex(decrypted_msg).replace('0x', '').replace('L', '').decode('hex')