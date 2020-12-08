try:
	import pikepdf
	import time
	import itertools

	characters = input(str("[*] Characters To Use: "))
	min_length = int(input("[*] Min lenght of combinations: "))
	max_length = int(input("[*] Max lenght of combinations: "))
	filename = input(str("[*] File name/path To Crack: "))

	if min_length > max_length:
		print ("[x] Please `min_length` must smaller or same as with `max_length`")
		exit(1)

	start_time = time.time()

	for n in range(min_length, max_length + 1):
		for xs in itertools.product(characters, repeat=n):
			password = ''.join(xs)
			print(f"[~] INFO: Trying {password}")

			try:
				with pikepdf.open(filename, password=password) as pdf:
					print("[✓] Password Found!")
					print(f"[✓] Password is {password}")
					print(f"[✓] Total Time Taken {(time.time() - start_time)}")
					exit(0)
			except pikepdf._qpdf.PasswordError as e:
				continue

	print("[x] All Combinations in the given criteria were\ntried, but password was not found")
	exit(0)
except KeyboardInterrupt:
	print("[x] Ctrl + C Detected")
	exit(0)
except ImportError:
	print("[x] Any Required Module Was Not Found, Most Probably 'pikepdf'\nTry pip3 install pikepdf or pip install pikepdf")
	exit(1)
except Exception as e:
	print(e)
	exit(1)
