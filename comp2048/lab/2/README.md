Links:
	'enigma doc' :
	'https://www.nsa.gov/Portals/70/documents/about/cryptologic-heritage/historical-figures-publications/publications/wwii/german_cipher.pdf',
	'david perry' :
	'https://www.realcty.org/wiki/Cryptology'
	'simon singh :: the code book' :
	'https://www.math.uci.edu/~brusso/freshman6.pdf'

Intro:

	Looking at some videos by numberphile and computerphile on utbe but havent really understood.
	Damn these brits cant explain for shit trying ucdavis lecture by some nerd from nsa says he works as a
	cryptologic mathematician / crypto analyst (yeah i cant spell for shit) David Perry, teaches cryptology
	and taught at lanchester penselvania at franklin marshal campus youtube.com/watch?v=ncL2Fl6prH8

Monoalphabetinc Substution Ciphers :: plain enclish __ letter for letter substution cipher:

	scrambellnig of the alphabet : premutation of the alphabet 26!

	a simple Caesar is a shift and there are 26 different to choose a shift

	Frequency analysis by arabs in 900ce

	The Vigenere Cipher: requires a agreed upon keyword thats written multipletime and each plaintext letter
				is mapped to its corresponding Caesar shift
				i.e. T mapes to V as A mapes to C i.e a shift of 3 letters
				H mapes to S as A mapes to L a shift of 10 lettes

		keyword: 	CLIMBCLIMBCLIM...
		plaintext:	THEREISNOLIMIT...
		ciphertext:	VSMDFKDVAMKXQF...

		symboltable:	+-/*&+-/*&+-/*...

				(---)(---)(---...

				essentially we in a big text we can see patterns after blocks because after the length of
				the keyword the shift is repeated
				from the patterns we can deduce which what may be the length of the keyword noteing the shortest
				pattern. Breaking the cipher text in to symbols and then we mathch it to normal english using freq
				analysis. After that we may deduce that the shift for each symbol taking samples
				say for example the + cipher text destribution and figure out the shift from that matching it with
				english language normal distribution i.e. e occurs max and stu occur okaish times then drop in freq for
				vwxy sharp drop and then for a spike i.e. a histogram to and try to shift our histo to match the normal
				one to figure out the shift for + symbol
				trial and error
				eventually for all symbols

Enigma: all of the above was motivation for the enigma; so we know how to crack vigenere cipher because of the keyword repeating
	now imagine the keyword spans for the entire text or theoretically anyway for a text for n size where n is reazonabelly large
