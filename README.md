# Password Generator with GUI

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GNU GPL v3 (see LICENSE).

A Python 3 password generator using the cryptographically secure `secrets` module, with a Tkinter desktop interface and a CLI. Passwords are generated only when requested, and lengths are validated (1–4096).

```sh
python3 PasswordGenerator.py
python3 PasswordGenerator.py --length 24
python3 -m unittest discover -s tests -v
```

The desktop version requires Python with Tkinter installed. No `easygui` or third-party Python dependency is needed. Avoid displaying generated passwords in recorded terminal sessions.

The original implementation is preserved on the [old branch](https://github.com/hamdyaea/PasswordGenerator-GUI/tree/old).
