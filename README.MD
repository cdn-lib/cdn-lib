<!-- 
PORTOFOLIO OF YUMEIRO DESU



-->







<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,26&height=200&section=header&text=YUME%20DEVELOPER&fontSize=52&fontColor=ffffff&animation=twinkling&fontAlignY=38&desc=Pengembang%20Web%20Full%20Stack%20from%20Indonesia&descAlignY=58&descSize=30&descColor=ccccff" alt="Header"/>

<div align="center">

<img src="waifu.gif" width="auto" alt="thumbnail"/>

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=20&duration=2800&pause=900&color=6C63FF&center=true&vCenter=true&width=650&lines=Yumeiro;Pengembang+PHP+dan+JavaScript+dari+Indonesia;Anime+%E2%80%A2+Kode+%E2%80%A2+Open+Source;Ayo+Buat+Sesuatu+Bersama" alt="Mengetik"/>

<br/>

<a href="https://animekita.online" target="_blank"><img src="https://img.shields.io/badge/Official Site-animekita.online-6C63FF?style=for-the-badge&logo=googlechrome&logoColor=white"/></a>

<a href="mailto:kaguraisempai@gmail.com"><img src="https://img.shields.io/badge/Gmail-Hubungi_Saya-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>

<a href="https://www.npmjs.com/~cdn-lib"><img src="https://img.shields.io/badge/npm-cdn--lib-CB3837?style=for-the-badge&logo=npm&logoColor=white"/></a>
</div>

---
# List Menu
<div align="center">

| | | |
| :---: | :---: | :---: |
| [**TENTANG**](#tentang-saya) | [**WAIFU**](#waifu-favorit) | [**TOOLS**](#alat-tempur) |
| [**PROYEK**](#proyek-berjalan-baru) | [**STATS**](#statistik-github) | [**ACHIVE**](#pencapaian) |

</div>

---
# TENTANG SAYA
RUN SENDIRI YA

```code
php yume.php
```

```php
<?php

class YumeDeveloper
{
    private const C_CYAN   = "\e[1;36m";
    private const C_GREEN  = "\e[1;32m";
    private const C_WHITE  = "\e[1;37m";
    private const C_YELLOW = "\e[1;33m";
    private const C_RED    = "\e[1;31m";
    private const C_RESET  = "\e[0m";

    public string $nama     = "Noval Ramdhani";
    public string $alias    = "YUME DEVELOPER";
    public string $pengguna = "cdn-lib";
    public string $lokasi   = "Indonesia";

    public array $stack = [
        "Programming" => ["PHP", "JavaScript", "Python 2.7", "Kotlin"],
        "Web Tech"    => ["HTML5", "CSS3", "jQuery", "Node.js"],
        "Environment" => ["Termux", "Linux", "Android Development"],
        "Expertise"   => ["API Integration", "Web Scraping", "UI/UX Design"]
    ];

    public array $proyekAktif = [
        "Official Site"   => "https://animekita.online",
        "Yumeiro Stream"  => "Anime Streaming Platform",
        "SMTP Mailer Kit" => "PHP Email Library",
        "Telegram Bot"    => "Server Monitor Tool",
    ];

    public function sedangBelajar(): array 
    {
        return ["Node.js", "Live2D Illustration", "Bahasa Jepang"];
    }

    private function getGithubMeta(): array
    {
        $url = "https://api.github.com/users/" . $this->pengguna;
        $opts = ["http" => ["method" => "GET", "header" => "User-Agent: PHP-Profile\r\n"]];
        $ctx  = stream_context_create($opts);
        $res  = @file_get_contents($url, false, $ctx);
        
        if ($res) {
            $data = json_decode($res, true);
            return [
                "Repositories" => $data['public_repos'] ?? 0,
                "Followers"    => $data['followers'] ?? 0,
                "Following"    => $data['following'] ?? 0,
                "Profile_URL"  => "github.com/" . $this->pengguna
            ];
        }
        return ["GitHub" => "Connection Failed / Offline"];
    }

    private function getSystemTelemetry(): array
    {
        return [
            "OS_KERNEL" => PHP_OS,
            "PHP_VER"   => phpversion(),
            "MEM_PEAK"  => round(memory_get_peak_usage() / 1024 / 1024, 2) . " MB",
            "ENGINE"    => "Zend Engine " . zend_version(),
            "STATUS"    => "System Operational"
        ];
    }

    private function drawLine(string $char = "-"): void
    {
        echo self::C_CYAN . str_repeat($char, 60) . "\n" . self::C_RESET;
    }

    public function build(): void
    {
        $telemetry = $this->getSystemTelemetry();
        $github    = $this->getGithubMeta();

        $this->drawLine("=");
        echo self::C_WHITE . " [ SYSTEM CORE ] : " . $this->alias . " | v2.1.0-STABLE\n" . self::C_RESET;
        $this->drawLine("=");

        echo self::C_GREEN . " ID_ENTITY\n" . self::C_RESET;
        printf("  %-15s : %s\n", "NAME", $this->nama);
        printf("  %-15s : %s\n", "LOCATION", $this->lokasi);
        printf("  %-15s : %s\n", "ALIAS", $this->pengguna);
        echo "\n";

        echo self::C_GREEN . " REMOTE_GIGTHUB_STATS\n" . self::C_RESET;
        foreach ($github as $key => $val) {
            printf("  %-15s : %s\n", $key, $val);
        }
        echo "\n";

        echo self::C_GREEN . " TECHNICAL_INFRASTRUCTURE\n" . self::C_RESET;
        foreach ($this->stack as $cat => $items) {
            printf("  %-15s : %s\n", $cat, implode(", ", $items));
        }
        echo "\n";

        echo self::C_GREEN . " DEPLOYED_PROJECTS\n" . self::C_RESET;
        foreach ($this->proyekAktif as $name => $desc) {
            printf("  * %-15s | %s\n", $name, $desc);
        }
        echo "\n";

        echo self::C_GREEN . " SYSTEM_TELEMETRY\n" . self::C_RESET;
        foreach ($telemetry as $key => $val) {
            printf("  %-15s : %s\n", $key, $val);
        }

        $this->drawLine("=");
        echo self::C_YELLOW . " TRANSMISSION COMPLETED\n" . self::C_RESET;
        $this->drawLine("=");
    }
}

$core = new YumeDeveloper();
$core->build();
?>
```

---

# WAIFU FAVORIT

<br/>

<div align="center">
<br/>

<a href="https://github.com/cdn-lib/cdn-lib">
  <img src="rezero-rem.gif" width="auto" alt="Rem - Re:Zero Animated"/>
</a>

<br/>

<table>
<tr>

<td align="center" width="300">

<img src="https://img.shields.io/badge/キャラクター-Karakter%20Art-6C63FF?style=flat-square&logo=anilist&logoColor=white"/>

<br/><br/>

<img src="rem.png" width="500" alt="Rem Art"/>

<br/>

<img src="https://img.shields.io/badge/レム-Rem-6C63FF?style=flat-square&logo=crunchyroll&logoColor=white"/>

</td>

<td valign="top">

<img src="https://img.shields.io/badge/Info-Karakter-6C63FF?style=flat-square&logo=anilist&logoColor=white"/>

```yaml
nama       : レム (Rem)
anime      : Re:Zero kara Hajimeru Isekai Seikatsu
ras        : Oni — 半鬼族 (Setengah Iblis)
pekerjaan  : Pelayan Istana Roswaal
senjata    : Gada Bola (Morning Star)
```

<img src="https://img.shields.io/badge/Seiyuu-Pengisi%20Suara-e91e8c?style=flat-square&logo=spotify&logoColor=white"/>

```yaml
nama       : 水瀬いのり (Minase Inori)
lahir      : 2 Desember 1994, Osaka, Jepang
agensi     : I'm Enterprise
peran_lain :
  - Isla     (Plastic Memories)
  - Yoshino  (Date A Live III)
  - Hinazuki (Boku dake ga Inai Machi)
```

<img src="https://img.shields.io/badge/Alasan_Suka-Kesetiaan%20dan%20Pengorbanan-0d1117?style=flat-square&logo=crunchyroll&logoColor=e91e8c"/>

```
Rem adalah simbol kesetiaan dan pengorbanan.
僕はレムが一番好き！
Tidak ada yang lebih setia dari Rem.
```

</td>
</tr>
</table>

<br/>

</div>

---

# ALAT TEMPUR

<div align="center">

<br/>

[![Ikon Keahlian](https://skillicons.dev/icons?i=php,js,html,css,git,github,vscode,linux,sqlite,npm,bash&theme=dark&perline=11)](https://skillicons.dev)

</div>

---

# PROYEK BERJALAN (BARU)

<br/>

<div align="center">

<a href="https://github.com/cdn-lib/smtp">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=cdn-lib&repo=smtp&theme=tokyonight&hide_border=true"/>
</a>

<a href="https://github.com/cdn-lib/ChatAIApp">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=cdn-lib&repo=ChatAIApp&theme=tokyonight&hide_border=true"/>
</a>

</div>

<br/>

| Proyek | Deskripsi | Stack |
|--------|-----------|-------|
| [**SMTP Mailer Kit**](https://github.com/cdn-lib/smtp) | Kit email PHP siap pakai — Kontak dan Langganan, balas otomatis, satu file konfigurasi | `PHP` `PHPMailer` `CSS` |
| [**ChatAI App**](https://github.com/cdn-lib/ChatAIApp) | Aplikasi chat bertenaga AI, dukungan banyak model | `JavaScript` `HTML` |
| [**KizunaNET**](https://animekita.online) | Platform konten anime dengan katalog produk dan checkout | `PHP` `SQLite` |

---

# STATISTIK GITHUB

<br/><br/>

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=cdn-lib&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true"/>

<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=cdn-lib&layout=compact&theme=tokyonight&hide_border=true&langs_count=6"/>

<br/>

<img src="https://streak-stats.demolab.com?user=cdn-lib&theme=tokyonight&hide_border=true"/>

<br/>

<img src="https://github-readme-activity-graph.vercel.app/graph?username=cdn-lib&theme=tokyo-night&hide_border=true&area=true" width="97%"/>

</div>

---

# PENCAPAIAN

<br/>

<div align="center">
  <img src="https://github-trophies.vercel.app/?username=cdn-lib&theme=tokyonight&no-frame=true&column=6&margin-w=8"/>
  <br/>
  <sub><i> </i></sub>
</div>

---

<div align="center">
# KATA-KATA HARI INI
<br/>

> *「どんなに辛くても、あきらめないでください」*
>
> **"Seberapa pun sulitnya, jangan pernah menyerah."**
>
> <img src="https://img.shields.io/badge/All%20Might-Boku%20no%20Hero%20Academia-6C63FF?style=flat-square&logo=myanimelist&logoColor=white"/>

</div>

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=3500&pause=1200&color=6C63FF&center=true&vCenter=true&width=540&lines=Arigatou+sudah+mampir;Kasih+bintang+kalau+suka+proyeknya;Mari+buat+sesuatu+yang+keren+bersama" alt="Footer Mengetik"/>

<br/>

<img src="https://img.shields.io/badge/Dari-Indonesia-DC143C?style=flat-square&logo=googlemaps&logoColor=white"/>

</div>

<!-- FOOTER BERGELOMBANG -->
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,20,26&height=120&section=footer" alt="Footer"/>
