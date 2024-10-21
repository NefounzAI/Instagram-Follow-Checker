import instaloader

def check_not_following_back(username, password):
    L = instaloader.Instaloader()

    try:
        print("Mencoba login tanpa 2FA...")
        L.login(username, password)
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("Autentikasi dua faktor diperlukan.")
        print("Kode telah dikirimkan ke perangkat Anda. Periksa SMS atau aplikasi autentikator Anda.")

        two_factor_code = input("Masukkan kode 2FA yang dikirimkan ke perangkat Anda: ")

        try:
            print("Mencoba login dengan 2FA...")
            L.two_factor_login(two_factor_code)
            print("Login berhasil dengan 2FA.") 
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            print("Kode 2FA salah atau gagal. Pastikan Anda menggunakan kode yang benar dan terbaru.")
            return
        except instaloader.exceptions.BadCredentialsException:
            print("Autentikasi gagal setelah memasukkan kode 2FA. Username atau password mungkin salah.")
            return
        except Exception as e:
            print(f"Error tidak terduga saat login 2FA: {e}")
            return

    except instaloader.exceptions.BadCredentialsException:
        print("Username atau password salah.")
        return
    except instaloader.exceptions.ConnectionException:
        print("Koneksi gagal.")
        return
    except Exception as e:
        print(f"Error tidak terduga: {e}")
        return

    try:
        profile = instaloader.Profile.from_username(L.context, username)

        followers = set(f.username for f in profile.get_followers())
        following = set(f.username for f in profile.get_followees())

        print(f"Jumlah followers: {len(followers)}")
        print(f"Jumlah following: {len(following)}")

        not_following_back = following - followers

        print("\nSemua pengguna yang Anda ikuti:")
        for user in following:
            print(user)

        print("\nSemua followers Anda:")
        for user in followers:
            print(user)

        if not_following_back:
            print("\nOrang yang tidak follow back:")
            for user in not_following_back:
                print(user)
        else:
            print("\nSemua orang yang kamu ikuti sudah follow back.")

    except instaloader.exceptions.ProfileNotFoundException:
        print(f"Profil dengan username '{username}' tidak ditemukan.")
        return
    except Exception as e:
        print(f"Error saat mendapatkan data profil: {e}")
        return

if __name__ == "__main__":
    username = input("Masukkan username Instagram Anda: ")
    password = input("Masukkan password Instagram Anda: ")

    check_not_following_back(username, password)
