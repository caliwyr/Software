# Data Privacy

- [Disclaimer](#disclaimer)
- [Technologies](#technologies)
- [Why be concerned?](#why-be-concerned)
- [Email](#email)
- [Internet Browser](#internet-browser)
- [Internet Services](#internet-services)
- [Search Engine](#search-engine)
- [Cloud Storage](#cloud-storage)
- [Cloud Docs](#cloud-docs)
- [Social Media](#social-media)
- [Messaging Apps](#messaging-apps)
- [Password Managers](#password-managers)
- [Smartphone / Tablet](#smartphone--tablet)
- [Computer](#computer)
- [VPN](#vpn)
- [DNS](#dns)
- [Cryptocurrency](#cryptocurrency)
- [Closing Notes](#closing-notes)
- [Appendix](#appendix)
    * [5 Eyes (avoid)](#5-eyes-avoid)
    * [9 Eyes (try to avoid)](#9-eyes-try-to-avoid)
    * [14 Eyes (try to avoid)](#14-eyes-try-to-avoid)
    * [Useful Websites](#useful-websites)

# Disclaimer
This document has not been written by an expert, and its contents may change upon discovering new information.

The intention is to:
- Highlight basic data privacy concerns.
- Collate a broad-spectrum of privacy related information.
- Provide a framework of understanding to build upon.

Please do your own research before acting upon these notes.

You’re welcome to copy, distribute, make suggestions, corrections or edits.

Whilst this document can be applied to any platform, some parts target macOS specifically.

# Technologies
These technologies may concern your privacy:

| **Technology** |
| --- |
| Email |
| Internet Browser |
| Search Engine |
| Cloud Storage |
| Social Media |
| Password Management |
| Software / Apps |
| Internet Service Provider (ISP) |
| Virtual Private Network (VPN) |
| Domain Name Service (DNS) |
| Media Access Control address (MAC) |

These technologies may apply to the following platforms:

| **Platform** |
| --- |
| Computer |
| Tablet |
| Smartphone |
| Smart home devices ([Internet of things - IoT](https://en.wikipedia.org/wiki/Internet_of_things)) |

# Why be concerned?
The National Security Agency (NSA) was shown to be [collecting data on a mass scale](https://www.theguardian.com/world/2013/jun/06/us-tech-giants-nsa-data) by Edward Snowden in 2013, under an operation code-named [PRISM](https://www.theverge.com/2013/7/17/4517480/nsa-spying-prism-surveillance-cheat-sheet). The operation outlines cooperation with major service providers (such as Apple, Facebook and [Google](https://twitter.com/DuckDuckGo/status/1371509053613084679/photo/1)), but also with the UK’s Government Communications Headquarters (GCHQ). Further cooperation between intelligence agencies has since been documented as the [Five Eyes, Nine Eyes and 14 Eyes](https://restoreprivacy.com/5-eyes-9-eyes-14-eyes/).

From 2013, arguably in light of this revelation, the UK took a [number of steps](https://en.wikipedia.org/wiki/Internet_censorship_in_the_United_Kingdom#History) towards stricter internet policing. In 2016, the UK passed the [Investigatory Powers Act](https://www.theguardian.com/world/2016/nov/29/snoopers-charter-bill-becomes-law-extending-uk-state-surveillance) to legalise and legitimise surveillance.

Digital services like Google and Facebook primarily model their business around [advertising](https://www.cleverism.com/google-business-model/), exploiting user data to serve highly targeted ads. The more data points deduced, the more targeted the ads. Whilst these models subsidise free services, the seemingly unregulated data access to [unsuspicious citizens](https://cdt.org/insights/section-702-what-it-is-how-it-works/), and its use by third parties such as [Cambridge Analytica](https://www.rightly.co.uk/blog/cambridge-analytica-explained/), is particularly worrisome.

It’s easy to say: ‘*I have nothing to hide...’*, but data allows technology to manipulate and polarise, which poses a real threat to society, as seen with the 2021 storming of the [United States Capitol](https://eu.usatoday.com/in-depth/news/2021/01/06/dc-protests-capitol-riot-trump-supporters-electoral-college-stolen-election/6568305002/). Social technologies may feign innocence, but their algorithms suggest the most engaging (or triggering) content based on your data. The more engaged (or triggered) you are, the longer you’ll stay, and the more ads you’ll potentially interact with.

Therefore, we should take responsibility and do whatever we can to protect our privacy, not just for ourselves, but also for society.

# Email
It’s worth reading up on the basics of [how email works](https://www.howtogeek.com/56002/htg-explains-how-does-email-work/), and [why it’s unsafe](https://www.securedocs.com/blog/how-secure-is-email).

[Encrypted email services](https://restoreprivacy.com/email/secure/) posit themselves as the answer, but you’ll most likely still send emails to recipients that don’t use these services. Whilst encrypted email services mitigate the monitoring of your personal account, emails can still be monitored on the recipient’s account. Edward Snowden suggests [not using them at all](https://twitter.com/snowden/status/1175437588129308672?lang=en).

The following questions should be asked before using an encrypted email service:
* Are emails encrypted at rest? And which parts are encrypted?
* How strong is the encryption?
* Is the jurisdiction outside of the [14 eyes](https://restoreprivacy.com/5-eyes-9-eyes-14-eyes/)? And if not, are logs kept?

If you want to switch service, and also maintain your contacts, emails and folders (labels), you could (depending on your current service):
* Export your emails to [mbox format](https://lifehacker.com/how-to-back-up-your-gmail-and-view-mbox-files-1827660389), and then import them into your new service. Alternatively you could try moving emails [folder by folder](https://posteo.de/en/help/moving-from-gmail-to-posteo#email) (including your sent folder) 50-100 at a time via [Thunderbird](https://www.thunderbird.net/en-GB/).
* Once imported, delete everything from the old provider.
* Change any services over to your new email address.
* Then either (slowly transition):
    - Indefinitely setup [message forwarding](https://support.google.com/mail/answer/10957) from the old address.
    - Create a [message filter](https://support.google.com/mail/answer/6579) to immediately delete the forwarded emails. *(Messages may be kept for some time in the trash before being permanently deleted.)*
    - Delete the old account after some time.
* Or (immediately transition):
    - [Mail merge](https://addons.thunderbird.net/en-US/thunderbird/addon/mail-merge/) your old contacts to notify them about your new email address.
    - Delete the old account.

To backup any email, either export it in mbox format from your email provider, or use Thunderbird (which can restore the folder locally later on). 
To use Thunderbird without any 3rd-party extension:
* Find the email's directory by clicking `Tools -> Account Settings -> Server Settings` and extracting the value from `Local Directory` (it may look something like: `.../Thunderbird/Profiles/<MY_PROFILE>.default/ImapMail/<MY.IMAP.ACCOUNT.COM>`).
* To backup everything:
    - Click on every folder in Thunderbird to ensure they're downloaded.
    - Zip up the entire folder.
    - Store it on an encrypted hard drive / cloud service.
* If you want to backup a specific folder:
    - Zip up the `<FOLDER_NAME>.msf` file, `<FOLDER_NAME>.sbd` folder (if it exists) and the empty `<FOLDER_NAME>` file. If the empty file doesn't exist, create one. 
    - Store it on an encrypted hard drive / cloud service.

To access the backup at a later stage in Thunderbird:
* Unzip the file
* Move its contents to: `/Thunderbird/Profiles/<MY_PROFILE>.default/Mail/Local Folders/`
* Restart Thunderbird and it should appear in the `Local Folders` section. If you can't this section, click `View -> Layout -> Folder Pane`.

You must then decide how to access your email. Whilst web browsers are commonplace, any time spent browsing leaves you more vulnerable to tracking. One solution is to use a software email client, such as [Thunderbird](https://www.thunderbird.net/en-GB/) which can be configured to prevent [web-beacons and tracking pixels](https://en.wikipedia.org/wiki/Web_beacon) ([more info](https://www.bbc.com/news/technology-56071437)). However, web clients store information on your computer, which can be a target for malware, or pose a security risk if your laptop is stolen.

If you want to keep your existing setup with minimal changes (e.g. everything works as before - notes, calendar, emails on your phone, etc), [Posteo](https://posteo.de/en) seems a good option. Whilst it’s a German company (within the 14 eyes), and German law is [becoming more worrisome](https://old.reddit.com/r/tutanota/comments/dwqqzs/tutanota_its_not_safe/), they don’t keep logs, even if they were almost forced to start logging [ip addresses](https://www.zdnet.com/article/log-free-email-provider-posteo-you-must-log-user-ip-addresses-court-rules/).

If keeping your existing emails isn’t a requirement, [Tutona](https://tutanota.com/) or [CTemplar](https://mail.ctemplar.com/signin) look promising. [CounterMail](https://countermail.com/) is the most secure option, but you’d need an invite from an existing user. 

If you request an invitation, do it from an anonymous account. Once your real name is associated with an invite code, your account becomes identifiable.

Once you choose a provider, use a number of [email aliases](https://www.techopedia.com/definition/1653/email-alias) to hide your main email address (never use the main address to send emails). For example, you could create an alias for friends, online services, and temporary aliases for anonymity. If you ever receive too much spam for a particular alias, you can safely delete it without affecting the main address. 

# Internet Browser
It’s worth reading the basics of how an [internet browser works](https://www.mozilla.org/en-GB/firefox/browsers/what-is-a-browser/).

[Firefox](https://www.mozilla.org/en-GB/firefox/new/) configured for maximum privacy (see [here](https://restoreprivacy.com/firefox-privacy/) and [here](https://www.privacytools.io/browsers/#about_config)) with some plugins ([NoScript](https://noscript.net/), [uBlock Origin](https://ublockorigin.com/), [Privacy Badger](https://privacybadger.org/) and [Decentraleyes](https://decentraleyes.org/)) is probably the fastest option for private browsing, but it won’t stop your [Internet Service Provider (ISP)](https://en.wikipedia.org/wiki/Internet_service_provider) from [tracking you](https://digital.com/online-privacy/isp-tracking/). For best privacy, use the [Tor Browser](https://www.torproject.org/) (also based on an earlier build of Firefox). Whilst it’s [harder for your ISP to track you](https://www.addictivetips.com/vpn/tor-usage-explained/) with the Tor Browser, they’ll still know you’re on the [Tor network](https://en.wikipedia.org/wiki/Tor_%28anonymity_network%29).

Firefox might seem unsafe, considering [Mozilla](https://www.mozilla.org) (its parent company) is a US company. However Firefox is open-source, renowned for privacy advocacy, and has a proven track-record for internet privacy.

Whichever browser you choose, clear its data often (every day, or every session). Alternatively, set the browser's data to clear automatically when it restarts, and restart it often.

Third parties can track you around the web in various ways:

| **Technology** | **How?** | **Ways to mitigate** | 
| --- | --- | --- |
| [Internet Protocol (IP) address](https://en.wikipedia.org/wiki/IP_address) | The IP address of your router will either be static (assigned by the ISP), or stay the same until you [restart the router](https://www.virginmediabusiness.co.uk/help-and-advice/products-and-services/static-and-dynamic-ip-addresses-explained/). The IP can be used as a unique identifier. | Use a VPN to hide your IP address from your ISP, and regularly change its server location to be something outside of the 14 eyes. For *best* privacy use the [Tor Browser](https://www.torproject.org/) over a VPN (i.e. start the VPN first, and then open the Tor Browser), or with a [bridge](https://tb-manual.torproject.org/bridges/). For *some* privacy, use Firefox over a trustable VPN. | 
| Accounts | Logging into accounts like Google or Facebook will allow them to track you around the web, even with private browsing on, due to the presence of [Google analytics](https://analytics.google.com/analytics/web/) and [Facebook like buttons](https://developers.facebook.com/docs/plugins/like-button/) on most web pages. | Log out of all unnecessary online services, clear the browser's data, and then restart the browser. | 
| [HTTP Referer](https://en.wikipedia.org/wiki/HTTP_referer) | The previous web page address that can be exploited by trackers. | [Turn it off](https://www.privacyinternational.org/guide-step/4148/change-http-referer-settings-firefox) | 
| [HTTPS](https://en.wikipedia.org/wiki/HTTPS) | HTTP sends unencrypted web traffic that could be [intercepted by an attacker](https://www.cloudflare.com/en-gb/learning/ssl/why-is-http-not-secure/). | Configure your browser to warn against accessing HTTP pages. Take extra care on public Wi-Fi networks (cafes, airports, etc). | 
| [Cookies](https://privacy.net/stop-cookies-tracking/) | Cookies are small pieces of information stored on your computer that can be used to identify you. | Block all third party cookies in your browser. Automatically delete cookies when the browser closes. Always send a ‘[do not track signal](https://spreadprivacy.com/do-not-track/)’ from your browser. | 
| [Web beacons / ](https://www.gdpreu.org/compliance/email-tracking/)[Tracking pixels](https://www.gdpreu.org/compliance/email-tracking/) | Hidden pixels that collect data about you. | Block them in all windows | 
| [Cryptominers](https://www.malwarebytes.com/cryptojacking/) | JavaScript that uses your system resources to mine crypto-currencies. | Block them in your browser. | 
| [Fingerprinters](https://pixelprivacy.com/resources/browser-fingerprinting/) | Non-obvious information that can be collected about you that creates a unique identification. To test your browser, visit: [Cover Your Tracks](https://coveryourtracks.eff.org/), [TorZillaPrint](https://arkenfox.github.io/TZP/tzp.html), [CreepJS](https://abrahamjuliot.github.io/creepjs/), [UNIQUEMACHINE](https://uniquemachine.org/), [AmIUnique](https://amiunique.org/) | Block them in your browser. Consider using these plugins: [NoScript](https://noscript.net/), [uBlock Origin](https://ublockorigin.com/), [Privacy Badger](https://privacybadger.org/) and [Decentraleyes](https://decentraleyes.org/) | 
| [Pop-up windows](http://www.bbc.co.uk/webwise/guides/about-popups) | Adverts that pop up without your permission or engagement. Often these can contain cryptominers, web-beacons and fingerprinters. They can also trick you into downloading malware. | Block them in your browser. | 
| Logins / passwords / auto-completions | Browsers make the user experience more fluid with auto-completion, but data gets populated without requiring a password. Even if it's setup to use a password, data gets stored locally. This risks exploitation by malware, and may pose a security risk if your laptop is stolen. | Never save them with your browser. If you need to save passwords or form data, use a separate encrypted password management service. | 
| History | Keeping history on the browser is at risk of exploitation from malware, and may pose a security risk if your laptop is stolen. | Never remember. Clear when the browser restarts. | 
| Search bar | The search bar normally defaults to a search engine, but can also search your bookmarks and history. | Don’t suggest anything in the search bar. Only use private search engines. | 
| Permissions | Permissions determine how the browser should handle requests for your computer’s hardware. | Remove any and all permissions. Never ‘always allow’. | 
| [Flash](https://www.adobe.com/products/flashplayer) | Flash enables animations and rich content to display in your browser, however it also can be used for [supercookies](https://blog.mozilla.org/security/2021/01/26/supercookie-protections/). | Uninstall it. Firefox [dropped Flash in version 85](https://www.pcgamer.com/firefox-update-kills-adobe-flash-support-and-protects-against-evil-supercookies/). | 
| [WebRTC](https://webrtc.org/) | WebRTC provides real-time communication capabilities (e.g. Google Hangouts), but can also [leak your IP](https://www.purevpn.com/webrtc-leak-test) over a VPN. | Disable [in the settings](https://www.ivacy.com/internet-privacy/disable-webrtc-leak/), or with a plugin like [Disable WebRTC](https://addons.mozilla.org/en-US/firefox/addon/happy-bonobo-disable-webrtc/). | 
| [User Agent](https://whatmyuseragent.com/) | The User Agent helps identify the browser and operating system. It can be exploited to help form a unique identifier. | It’s not always clear what the best option is, as a normal user agent might blend you into the crowd. Nonetheless it can be [hidden](https://support.mozilla.org/en-US/kb/how-reset-default-user-agent-firefox) or [spoofed](https://stackpointer.io/software/user-agent-spoofing-with-firefox/108/). You can check how it appears [here](https://whatmyuseragent.com/). | 
| Browser plugins | Whilst browser plugins add extra capabilities, plugins from third parties may collect your data, or act as malware. | Less is more with plugins. Beware of plugins that require unexpected (or too many) permissions. | 
| Authentication | Simple website logins are susceptible to [keyloggers](https://www.mcafee.com/blogs/consumer/family-safety/what-is-a-keylogger/) and [password leaks](https://haveibeenpwned.com/PwnedWebsites). | Where possible, use two-step authentication with an [OTP (one time-password)](https://en.wikipedia.org/wiki/One-time_password) app like [FreeOTP](https://github.com/freeotp). Don’t use Google’s authenticator app. _Always download backup codes in case you lose your phone_. | 
| [Media Access Control (MAC) address](https://whatismyipaddress.com/mac-address) | The hardware address of your network adapter that can be used to identify you. | The MAC address should be [spoofed](https://nordvpn.com/blog/mac-address/) regularly. *MAC addresses can [no longer be changed](https://developer.apple.com/forums/thread/654452) on Big Sur.* | 
| [Domain Name Service (DNS)](https://www.cloudflare.com/en-gb/learning/dns/what-is-dns/) | The DNS converts human friendly web addresses into IP addresses over HTTP, which can cause [IP leaks](https://vpnonline.com/guides/what-is-dns-leak-and-how-to-fix-it/) over a VPN. | Check your VPN prevents DNS leaks, and [test](https://www.dnsleaktest.com/) their claim. Various tools like [dnscrypt](https://dnscrypt.info/) ([macOS tutorial](https://github.com/larromba/macOS-Security-and-Privacy-Guide#dnscrypt)) can help encrypt DNS traffic. On Firefox you can enable DNS over HTTPS, using an alternative DNS than that provided by your ISP (like [LibreDNS](https://libredns.gr/)). | 
| [hosts file](https://en.wikipedia.org/wiki/Hosts_%28file%29) | The hosts file acts like a local DNS, and can be a useful way to block urls of known trackers, adwares or malwares. | There’s lots of examples online, like [this one](https://github.com/1r2/iosparanoid). | 

# Internet Services
The less time you spend on the internet, the better. If you must be online, where possible:
* Limit social media usage. Your time equates to the data social media exploits.
* If no VPN is present:
    - Stay logged out of your accounts.
    - Use a private tab.
    - Use a trusted network (like your home network).
    - Use HTTPS.
    - When finished, clear the browser's history, and then close the browser.
* Only sign up to services you really need. For anything else, consider using a [throw-away email address](https://temp-mail.org/en/), or a temporary [email alias](https://www.techopedia.com/definition/1653/email-alias).
* Don’t always use the same username.
* Be sure to delete unused accounts where possible.
* Use a password management service to maintain strong and unique passwords. It’ll also act as a record of any services you’ve signed up to.
* Register important email addresses on [haveibeenpwned](https://haveibeenpwned.com).

# Search Engine
There’s no doubt Google is the best and most intuitive search engine, but it’s at the expense of tracking you, and [keeping logs forever](https://www.siliconvalleywatcher.com/google-keeps-your-data-forever---unlocking-the-future-transparency-of-your-past/). Ideally you’ll want to replace Google with something else, and only it when absolutely necessary.

[DuckDuckGo](https://duckduckgo.com/) has arguably become the most well-known private search engine. It also returns fairly decent searches. Nonetheless it has a troubling past (see [here](https://lemmy.ml/post/31321) and [here](http://Techrights.org/2020/07/02/ddg-privacy-abuser-in-disguise/)) and may have once tried to secretly [fingerprint](https://betanews.com/2019/01/07/duckduckgo-fingerprinting-accusation/#comments) users. Regardless, it’s still a better choice than Google

There’s a few more alternatives described [here](https://restoreprivacy.com/private-search-engine/), but none of them seem too convincing. For a more broad comparison, [this](https://searchengine.party/) may help.

You’ll definitely want to avoid:
* [OneSearch](https://www.onesearch.com/) (owned by Verizon Media, USA), as they save your IP address and search queries for 4 days.
* [Private.sh](https://private.sh/) as they’re owned by Kape technologies, formally known as Crossrider (who have a track record of including [malware in their products](https://restoreprivacy.com/private-internet-access-kape-crossrider/)).
* [Presearch.io](https://www.presearch.io/) as they have too many clauses on how they [may share your information](https://www.presearch.org/privacy).

From further research, here’s an analysis of private search engines that might be worth trying:

| **Search Engine** | **Data Tracked / Logged** | **Potential Issues** | **Server / Company Location** | 
| --- | --- | --- | --- |
| [Metager](https://metager.org/) | Stores IPs for 4 days. Search is cached for a few hours. Tracks language selection, search settings, accept header (for statistics). | Two blocks of the IP address and the user agent are given to advertisers. | Germany |
| [Swisscows](https://swisscows.com) | Removes IP and user agent from search terms after 7 days. | Filters adult / abusive content. Some data is transmitted to advertising partners. | Switzerland | 
| [Peekier](https://peekier.com/) | HTTP Referrer, search queries (temporarily), HTML5 local storage (for settings). | Single session cookie on Cloudflare. Weird layout. | Panama | 
| [InfinitySearch](https://infinitysearch.co/) | HTTP Referrer | Might leak data to Cloudflare. Poor searches. | Innovare Technologies (USA). | 
| [Oscobo](https://www.oscobo.com/) | Supposedly nothing. | Uses cookies to encrypt search terms on the browser. Uses proprietary technology. Privacy links in _[8. More Information](https://www.oscobo.com/ctnt.php?c=privacy)_ are strange. | UK | 
| [Mojeek](https://www.mojeek.com/) | Time of visit, page requested, HTTP Referrer, two letter country code. | _Not clear._ | UK | 
| [Disconnect](https://search.disconnect.me/) | Imprecise geo-location information, page views, browser type, operating systems, site inks. | Doesn’t respond to ‘do not track’ settings. Stores first-party browser cookie to remember preferences. States it might serve legal requests. | Delaware, USA | 
| [Tailcat](https://meow.tailcat.com/) | _Not stated._ | _No policy._ [Can it be trusted?](https://news.ycombinator.com/item?id=25807094) | _Not clear_ - hosted by Cloudflare (USA). | 
| [Whoogle](https://whoogle.himiko.cloud/) ([github](https://github.com/benbusby/whoogle-search)) | _Not stated._ | _No policy._ Can the [public instance](https://whoogle.himiko.cloud/) be trusted? | Amsterdam (public instance) | 
| [Startpage](https://www.startpage.com) | Operating system, times accessed, browser type, language, IP address (robots only) | [Troubling parent company](https://restoreprivacy.com/startpage-system1-privacy-one-group/). | Netherlands | 

From this list, self-hosting [Whoogle](https://whoogle.himiko.cloud/) (instructions [here](https://github.com/benbusby/whoogle-search)) seems the safest option that most resembles a Google search. However, when Google updates its code, there may be breaking changes that must be fixed by the owner, and then applied yourself.

Out of the hosted options, [Peekier](https://peekier.com/) seems the most trustable, with decent searches, and a likeable server location. If the layout is too unusual, either [Metager](https://metager.org/) or [Mojeek](https://www.mojeek.com/) will seem more familiar. Metager has a better server location, but at the expense of sharing (fairly anonymous) data to advertisers.

Whichever search engine you choose, use a VPN (with encrypted DNS) or the Tor Browser to hide searches from your ISP.

# Cloud Storage
[Google Drive](https://www.google.com/drive/) and [Dropbox](https://www.dropbox.com) are commonly used for cloud storage, but it’s at the [expense of your data](https://www.wired.com/story/dropbox-sharing-data-study-ethics/).

There are [numerous encrypted options](https://restoreprivacy.com/cloud-storage/reviews/) on the market (detailed [here](https://restoreprivacy.com/cloud-storage/best/) and [here](https://www.macobserver.com/tips/quick-tip/5-encrypted-cloud-storage/)), but they all seem to have drawbacks.

[SpiderOak](https://spideroak.com/) was [championed by Edward Snowden](https://www.guidingtech.com/31680/dropbox-vs-google-drive-vs-spideroak/), but as it uses proprietary software, and is based in the US, there's always a worry of NSA cooperation. However, as the security looks very convincing, this worry is most likely paranoia.

[Koofr](https://koofr.eu/) (based in Ljubljana) might be a safer alternative. It has a simple [privacy pledge](https://koofr.eu/privacy/), and [this review](https://cloudstorageinfo.org/koofr-review) suggests client-side encryption is possible using [rclone](https://rclone.org/koofr/). If you don't want to use rclone, then you may find the desktop app [has issues](https://www.cloudwards.net/review/koofr/).

[NordLocker](https://nordlocker.com/) might be an option, but it seems more focused on encryption, rather than cloud storage. Nord is best known for their [VPN](https://nordvpn.com/). If you’re already using that, using another Nord product isn’t ideal, as privacy is arguably improved with diversity. There's a few videos on YouTube of the macOS desktop app asking for far too many permissions, [which is concerning](https://www.finjanmobile.com/app-permissions-the-good-the-bad-and-why-you-need-to-pay-attention/)). NordLocker will also track [anonymised app diagnostics](https://restoreprivacy.com/cloud-storage/reviews/nordlocker/). 

The most paranoid solution would be to self-host [NextCloud](https://nextcloud.com/), and encrypt files with [Boxcryptor](https://www.boxcryptor.com/en/) (reviewed [here](https://www.cloudwards.net/boxcryptor-review/)) or [VeraCrypt](https://www.veracrypt.fr/en/Home.html) (reviewed [here](https://www.cloudwards.net/veracrypt-review/)). However, if you incorrectly configure the server, it's still riskier than using an existing service. Existing services also have dedicated teams that keep up-to-date with the latest security practises.

# Cloud Docs
If you're using Google Drive, before transferring to another service, you'll first need to untangle yourself from Google's placeholder files (`.gdoc`, `.gsheet`, etc). Searching for these extensions within your desktop's Google Drive folder will help identify which documents need to be transferred.

Unless you need group collaboration, or future-proofing, the simplest solution would be to export your cloud docs to a native extension (e.g. `.odt` / `.docx`) and edit them on your computer using proprietary software (like [Pages](https://www.apple.com/pages/) or [Numbers](https://www.apple.com/numbers/) for macOS), or if portability is a requirement, an open-source software (like [OpenOffice](https://www.openoffice.org/) or [LibreOffice](https://www.libreoffice.org/)). Files can then be synced to the cloud via a folder on your computer.

Unfortunately most privacy-based alternatives seem at the expense of feature compatibility and usability, but if you need a simple replacement that's fairly privacy-savvy, [CryptPad](https://cryptpad.fr) is probably your best bet. Whilst based in France ([9 eyes](#9-eyes-try-to-avoid)), their character seems noble; during the Pandemic CryptPad added this to their home-page:

```
In the current health crisis linked to the COVID-19 outbreak, CryptPad supports remote working. The storage limit for all registered users is increased to 1GB until further notice. Registration is free with no personal data required.
```

CryptPad's most lacklustre feature seems to be the presentations (see [this review](https://nixfaq.org/2020/09/can-it-replace-google-docs-cryptpad-review.html)), but the docs / spreadsheets will suffice for simple things. On signup, there's a notice stating links must be shared securely (because they could potentially be guessed), and data-integrity isn't necessarily guaranteed (e.g. regular backups should be made).

For something more feature-rich and user-friendly, [Arcane Office](https://arcaneoffice.com/) is worth a look. However, their [Privacy Policy](https://cdn.arcaneoffice.com/TERMS.txt) does state the use of Google Ads alongside some minor logging.

A more detailed list of alternatives is available [here](https://www.techspot.com/news/80729-complete-list-alternatives-all-google-products.html) - _section: `Google Docs / Sheets / Slides alternative`_.

# Photos
There doesn’t seem to be much information about secure / private photo services, but a few are listed [here](https://www.techspot.com/news/80729-complete-list-alternatives-all-google-products.html).

Most solutions are self-hosted, requiring know-how and maintenance.

[Cryptee](https://crypt.ee/) is the only existing solution (and probably the most attractive), as it’s based in Estonia (outside of the 14 eyes), and run by a small team that seem passionate about privacy.

# Social Media
The best option is to simply limit, or forego all social media use.

Posting about your life is not just great for friends, but also intelligence agencies. Flippantly posting things can damage your life, your reputation and your job prospects; the internet is forever and unforgiving.

One solution is to use social media for business endeavours only, as professionalism helps to rein in the tongue.

You can deactivate Facebook to keep Messenger (if you need it), but Facebook will still have your data. The best option is to delete Facebook, alongside sending a [data removal request email](https://www.datarequests.org/blog/sample-letter-gdpr-erasure-request/).

# Messaging Apps
As WhatsApp is owned by Facebook, and considering the recent changes to their [terms and conditions](https://conversation.which.co.uk/technology/whatsapp-new-terms-conditions-privacy/), it’s advisable to use is sparingly, which is difficult due to its popularity. One solution is to find an encrypted messaging app (on Android and iOS), and ask your friends to use that.

There are a number of secure messaging apps detailed [here](https://restoreprivacy.com/secure-encrypted-messaging-apps/), [here](https://www.privacytools.io/software/real-time-communication/) and [here](https://www.techspot.com/news/80729-complete-list-alternatives-all-google-products.html). There’s a very comprehensive list [here](https://securechatguide.org/centralizedapps.html).

[Signal](https://signal.org/) (endorsed by Edward Snowden) is touted as one of the best encrypted messaging apps. Whilst Signal uses centralised servers based in the US, it’s open-source, and looks the most established, proven and trustable messaging app ([review here](https://restoreprivacy.com/secure-encrypted-messaging-apps/signal/)). As it's the most similar to WhatsApp, it's probably one of the easier alternatives to convince your friends to use.

[Session](https://getsession.org/) is a fork of Signal that doesn't require any details to register. However, from reading [this](https://restoreprivacy.com/secure-encrypted-messaging-apps/session/), there seems to be some concerns regarding the company's location in Australia, and if the product is even stable.

[Element](https://element.io/) uses a decentralised open-source network called [Matrix](https://matrix.org/), and doesn't [mine data](https://element.io/personal). However, when looking closer at the terms, it seems some [data collection and ip logging](https://element.io/privacy) does actually occur. The UI also seems a bit lacking, but if you prefer pseudo-anonymous sign-ups (no email or phone number), and more decentralisation, this seems a great choice.

There’s a long thread about Element [here](https://news.ycombinator.com/item?id=23842179). In the thread, [Syphon](https://syphon.org/) is suggested - an open-source app using the same Matrix network. However it’s only maintained by one developer, meaning the implementation might be harder to trust.

[Threema](https://threema.ch/en) (location in Switzerland) looks like an ideal alternative. However, as it’s paid-only, convincing your friends to use it will be very difficult.

[Status](https://status.im) (reviewed [here](https://proprivacy.com/privacy-service/review/statusim)) is worth a mention because of its [pseudo-anonymous account creation](https://status.im/security/). The company is also based in Switzerland. However it seems bloated with a few extra features (a browser and a crypto-currency wallet).

# Password Managers
It would be incredibly difficult, if not impossible to remember unique passwords for every service you use. A naive solution might be to write them down on paper, or save them in a text file, but storing passwords in ‘plain-text’ can be easily lost or stolen.

Password managers offer two different solutions to this problem, by saving encrypted passwords on a secure server, or by generating them from a function of inputs (e.g. website address + user name + master password). Deterministic password managers require no data to be stored anywhere, as they’re calculated on the fly.

There are pros and cons to each approach. Storing passwords on a server allows for completely random passwords, and keeps a record of the services you use. However, it’s all at the cost of a) trusting someone with your data, and b) trusting their servers are secure. Many password managers are also based in the US.

Deterministic password solutions _seem_ better because no one is trusted with your data, but if your ‘master password’ is discovered (e.g. via keylogging software), an attacker could potentially crack all your passwords by function of its inputs (e.g. by also finding out your username, and the service's website address). You’d also have to remember different inputs for every service, especially if you use multiple usernames.

There’s a list of password managers outlined [here](https://restoreprivacy.com/password-manager/best/) and [here](https://www.privacytools.io/software/passwords/).

Self-hosting [Bitwarden](https://bitwarden.com/) is probably the best option, as even though Bitwarden is a US company, its software is open-source. However, self-hosting is time-consuming to maintain, and can be configured insecurely. If you don’t want to self-host, Bitwarden is still better than [LastPass](https://www.lastpass.com/), as LastPass uses proprietary software, and its parent company [LogMeIn](https://www.logmein.com) was [acquired by private US equity firms](https://restoreprivacy.com/password-manager/reviews/lastpass/).

If you have a bit of technical knowledge, [Pass](https://www.passwordstore.org/) (tutorial [here](https://gist.github.com/flbuddymooreiv/a4f24da7e0c3552942ff)) is the simplest (and most elegant) solution using [GPG](https://rtcamp.com/tutorials/linux/gpg-keys/). Whilst Pass is programmed in bash, it’s [open-source](https://git.zx2c4.com/password-store/), well [unit-tested](https://git.zx2c4.com/password-store/tree/tests) and seems to have a nice community.

However, storing encrypted passwords locally is a target for malware, especially as your GPG-key’s passphrase could be caught by key-loggers. Keylogging concerns any service, but services like Bitwarden mitigate it with additional measures, such as preventing log-ins from different IP addresses, and two-step authentication. Two-step authentication seems possible with Pass using a [YubiKey](https://www.yubico.com/products/yubikey-hardware/yubikey-neo/), but the setup looks complex (see [here](https://karlgrz.com/2fa-gpg-ssh-keys-with-pass-and-yubikey-neo/), [here](https://ocramius.github.io/blog/yubikey-for-ssh-gpg-git-and-local-login/) and [here](https://captnemo.in/blog/2020/01/04/security-setup/)). The GPG key could be kept on a remote server and temporarily downloaded via [SSH using two-step authentication](https://www.techrepublic.com/article/how-to-set-up-2-step-authentication-for-ssh-on-your-linux-servers/), but Pass might need to be modified.

If you use Pass, it would be wise to [backup your GPG key](https://risanb.com/code/backup-restore-gpg-key/), as if it’s lost, your passwords are toast. Using a [faux password](https://www.digitalneanderthal.com/post/gpg/) on the local key would keep any backups safe, as a compromised faux password won't affect the backup.

Hosting encrypted passwords on a private GitHub repo is _probably_ ok, but GitHub is a US company. Hosting your own private GitHub repo might be more secure, but it comes with the same maintainability / configuration issues as explained above.

# Smartphone / Tablet
It’s much easier to lock-down your laptop than your smartphone or tablet, as these can be [easily identified](https://citizenlab.ca/2015/05/the-many-identifiers-in-our-pocket-a-primer-on-mobile-privacy-and-security/). This is concerning seeing as mobile devices are becoming evermore ubiquitous.

Phone-calls and messages are normally sent unencrypted, so it’s best to avoid these methods of communication, and only use encrypted apps where possible.

Try to replace any Google-apps with (preferably open-source) [alternatives](https://alternativeto.net/).

A VPN and encrypted DNS can help hide your IP address from your ISP. Changing your DNS server can also help to block ads and trackers. [LibreDNS](https://libredns.gr/) (tutorial [here](https://gitlab.com/libreops/libredns/libredns.gr/-/wikis/home)) seems a good example, as it’s open source and based in Germany.

Smartphone browsers aren’t very customisable, so something designed for additional privacy should be used, like ~~[Firefox Focus](https://support.mozilla.org/en-US/kb/focus)~~ [Brave](https://brave.com/download/) with all the 'privacy shields' activated. The default search engine should be changed to something more private.

It’s worth knowing that your phone can't be made private, because of two unique identifiers: the [IMEI](https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity) (International Mobile Equipment Identity) and [IMSI](https://en.wikipedia.org/wiki/International_mobile_subscriber_identity) (Individual Manufacturer Subscriber Identity).

The IMSI (burnt into your SIM card) is used by cell phone towers when connecting you to a network, which [leaks your location](https://observer.com/2019/10/edward-snowden-smartphone-surveillance-joe-rogan-podcast/). Cell phone towers keep recrods [for a long time](https://www.forensicfocus.com/articles/cellular-provider-record-retention-periods/), and authorities (or [third parties](https://www.paladion.net/blogs/how-to-build-an-imsi-catcher-to-intercept-gsm-traffic)) can use [IMSI-capture](https://www.firstpoint-mg.com/blog/top-7-imsi-catcher-detection-solutions-2020/) devices to intercept them.

Turning off your phone (or using airplane mode) [won’t solve this](https://www.businessinsider.com/edward-snowden-phone-2016-7?r=US&IR=T). The only solution is to use a [burner phone](https://www.fifthgeek.com/whats-a-burner-phone-how-much-does-a-burner-phone-cost/), or nothing at all.

If you use an iPhone, [don't jailbreak it](https://www.howtogeek.com/227214/why-you-shouldn%E2%80%99t-jailbreak-your-iphone/). It may [remove protections](https://www.intego.com/mac-security-blog/dont-jailbreak-your-iphone-if-you-want-to-stop-government-spyware/) that keep you safe from third-party developers.

It's probably worth getting a [phone camera cover](https://www.amazon.com/s?k=phone+camera+cover).

# Computer
Generally you should only download and run programs from verified developers.

Anything downloaded from browser pop-ups (especially Flash installers) are [probably malware](https://www.wired.com/story/mac-malware-flash-installer-onlyfans-pirates-netgear-zero-day-security-news/). Downloading cracked programs from P2P file-sharing services (like BitTorrent) are likely to [contain malware](https://cybersecurityportal.com/cracked-games-contain-viruses-malware/).

Malware typically infects and then persists, by either living in plain sight, or by evading detection. If you use macOS, [Patrick Wardle](https://twitter.com/patrickwardle) provides [free tools](https://objective-see.com/) to help diagnose and remove malware. He outlines the [basics of macOS malware](https://www.youtube.com/watch?v=fv4l9yAL2sU) at the 2015 Black Hat Conference.

Beware of 'free' virus scanners. They're normally given full-access to your computer, which is concerning as they may [sell your data](https://www.zdnet.com/article/avg-releases-transparent-privacy-policy-yes-we-will-sell-your-data/).

To improve macOS security, there’s lots of useful information collected in guides like [this](https://github.com/larromba/macOS-Security-and-Privacy-Guide) and [this](https://github.com/larromba/osx-security-awesome).

Unless you use Linux, there’s a good chance Microsoft / Apple will collect your data. Regardless, here’s some steps to improve your computer’s privacy:
* Use a private browser (like Firefox or the Tor Browser).
* Use a VPN (that prevents DNS leaks) or the Tor Browser to hide data from your ISP.
* [Encrypt outgoing DNS traffic](https://github.com/larromba/macOS-Security-and-Privacy-Guide#dnscrypt), or at least [encrypt outgoing DNS traffic over HTTPS](https://libredns.gr/) in your browser. _(This might not be compatible with your VPN)_.
* When on a public network, ensure your web traffic only [passes through a VPN](https://gist.github.com/scy/8122924) (i.e. the internet won’t work if the VPN is turned off).
* Update the [hosts file](https://github.com/larromba/iosparanoid) to block known adwares, malwares and trackers.

More information on improving macOS security can be found [here](https://github.com/larromba/osx-security-awesome).

It's probably worth getting a [webcam cover](https://www.amazon.com/s?k=webcam+cover).

# VPN
It’s worth reading [this](https://gist.github.com/joepie91/5a9909939e6ce7d09e29), [this](https://overengineer.dev/blog/2019/04/08/very-precarious-narrative.html) and [this](https://privacytools.io/providers/vpn/#info) to understand why VPNs don’t provide total anonymity.

VPNs help to:
* Ensure traffic is encrypted on a public network.
* Circumvent geo-locking by hiding the content’s IP address (the ISP will only see the VPN server's IP address).
* Add an additional layer of privacy when running Tor over VPN (but [bridges](https://tb-manual.torproject.org/bridges/) might still be a better solution).

VPNs won’t:
* Encrypt HTTP requests after they leave the VPN’s servers.
* Prevent you from being tracked by a service like Google if you login through a VPN.
* Always change your DNS settings. If you use your ISP’s default DNS settings (accessed via HTTP), your ISP will still see the webpages being accessed.
* Always adhere to ‘no log’ policies. It’s very rare to find a VPN that doesn’t log something. If the VPN’s jurisdiction is within the 14 eyes, logs may be handed over to authorities (by force, or through agreement).

It’s worth researching VPNs and their parent companies before purchasing one. For example, [Cyberghost](http://cyberghostvpn.com/) and [Zenmate](https://zenmate.com/) were both [purchased by Kape Technologies](https://restoreprivacy.com/private-internet-access-kape-crossrider/), formerly known as Crossrider, who bundled [malware](https://blog.malwarebytes.com/detections/adware-crossrider/) in their products. One of the CEOs (Koby Menachemi) may have been part of [Unit 8200](https://www.forbes.com/sites/thomasbrewster/2015/06/09/from-israel-unit-8200-to-ad-men/) (the Israeli version of the NSA / GCHQ).

Here’s some other [VPNs to avoid](https://www.makeuseof.com/tag/avoid-bad-vpns/).

A list of worthy VPN services are listed [here](https://privacytools.io/providers/vpn/#info) and [here](https://restoreprivacy.com/).

Out of these, [Mullvad](https://mullvad.net/en/) seems one of the better choices, perhaps validated by [Mozilla VPN's](https://vpn.mozilla.org/) decision to use their servers and technology. The Mullvad website also has a [Tor address](http://xcln5hkbriyklr6n.onion/), and allows payment with cryptocurrency. Whilst they tout no-logs, they’re still based in Sweden (part of the 14 eyes), which is concerning considering the [Sweedsh Court Surveillance of Data Act](https://mullvad.net/en/help/swedish-covert-surveillance-data-act/) came into force on 1st April 2020.

[IPVN](https://www.ivpn.net/) is based in Gibraltar (questionably outside of the 14 eyes, see [here](https://www.ivpn.net/blog/should-gibraltar-be-classified-as-a-member-of-the-five-eyes-alliance/) and [here](https://www.reddit.com/r/VPN/comments/421973/should_gibraltar_be_classified_as_a_fourteen_eyes/)) and has been [audited for no logs](https://cure53.de/audit-report_ivpn.pdf). However, it seems they track some [minor analytics](https://www.ivpn.net/knowledgebase/privacy/what-information-is-collected-and-stored-about-all-visitors-to-your-website/) on their website (including a redacted IP), so truly anonymous payments might be trickier.

If it’s difficult to decide, both services can be purchased for a single month in succession. Comparison charts are also available [here](https://www.safetydetectives.com/best-vpns/) and [here](https://www.vpnspy.net/).

# DNS
If you don't want to use a VPN, it’s worth trying to encrypt outgoing DNS traffic, as it’s normally done over HTTP. There are two things to encrypt - _DNS over TLS_ and _DNS over HTTPS_.

On macOS, [dnscrypt-proxy](https://github.com/DNSCrypt/dnscrypt-proxy) could be used in conjunction with [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) (see [tutorial](https://github.com/larromba/macOS-Security-and-Privacy-Guide#dnscrypt)).

Alternatively, DNS over TLS could be configured with [knot-resolver](https://www.knot-resolver.cz/) (see [tutorial](https://phiffer.org/2018/04/02/dns-over-tls-on-macos)), and DNS over HTTPS by setting your browser to use something from [this list](https://www.privacytools.io/providers/dns/). [LibreDNS](https://libredns.gr/) seems a solid choice.

# Cryptocurrency
If used properly, cryptocurrencies help to preserve your privacy whilst making a purchase.

Cryptocurrency transactions are chained together in a public, decentralised [blockchain](https://www.investopedia.com/terms/b/blockchain.asp). As it's public, every [transaction](https://www.blockchain.com/btc/tx/645989b3d3df37827f4dfe2f75bf2fea1e66e25d2c6c562225c0123d1567f429) includes information like IP addresses, [transaction addresses](https://www.blockchain.com/btc/address/1KyeBoM2XveqjHUQEcK3qgaxnn1bDFMvwU), and the transaction's value.

[Wallets](https://www.bitdegree.org/crypto/tutorials/cryptocurrency-wallet#a-brief-of-crypto-wallet) use a private key to access a transaction address' value. Modern [hierarchical deterministic (HD)](https://bitcoin.stackexchange.com/questions/98502/how-can-a-user-or-wallet-have-multiple-addresses-at-all-if-out-of-a-private-key) wallets use the same private key for various addresses, rather than creating new keys for each address.

As the identity of transactions and wallets aren't clear, cryptocurrencies are considered [pseudonymous](https://dictionary.cambridge.org/dictionary/english/pseudonymous). Pseudonymity shouldn't be confused with anonymity, as cryptocurrencies [aren't totally anonymous](https://99bitcoins.com/bitcoin-actually-anonymous/). As [regulations](https://www.finder.com/my/global-cryptocurrency-regulations) become tighter, anonymity becomes harder.

If you're looking to buy some small amounts of bitcoin to make anonymous transactions, you'll first need a [privacy focused wallet](https://bitcoin.org/en/choose-your-wallet?step=5). [Blockstream Green](https://blockstream.com/green/) is a good example, as it has an option to use the Tor network built in.

You'll then need to swap fiat money for cryptocurrency, which is very difficult. Never buy cryptocurrency from an exchange with [Know Your Customer (KYC)](https://www.cryptovantage.com/guides/know-your-customer/), as you'll need to provide identification. A list of exchanges without KYC can be found [here](https://tradingbrowser.com/crypto-exchange-without-kyc/), however most of them probably require some level of KYC (email, phone number, etc), and may ask for further identification at any stage.

There exist [other options](https://99bitcoins.com/buy-bitcoin/anonymously-without-id/) to buy anonymous cryptocurrency, but most of them have significant drawbacks. Depending on your country, swapping cash for cryptocurrency at [cryptocurrency ATMs](https://99bitcoins.com/buy-bitcoin/anonymously-without-id/#atm) is probably the easiest (and safest) way to avoid KYC ([map here](https://coinatmradar.com/)), especially for smaller amounts.

If you can't find an ATM without KYC, your best bet is to sign up to a cryptocurrency trading website (like [Hodl Hodl](https://www.hodlhodl.com), or [Paxful](https://paxful.com/)). If you do this, use an alias email address, fake username, and if you must provide a phone number, use a discardable SIM. Beware these platforms are prone to scams, and it can take time to find a reputable seller, or complete a transaction.

If this seems too unsafe, whilst unsavoury, it's possible to buy through the KYC process, and then use a [mixing service](https://www.worldcryptoindex.com/what-is-a-coin-mixer/) like [bitcoinmixer.io](https://bitcoinmixer.io) ([more listed here](https://bestbitcoinmixers.com/)) to obfuscate transaction relationships with algorithms like [CoinJoin](https://en.bitcoin.it/wiki/CoinJoin).

After purchasing some cryptocurrency, the transaction requires a number of [confirmations](https://cryptocurrencyfacts.com/what-are-confirmations/) (through a process of [mining](https://www.webopedia.com/definitions/cryptocurrency-mining/)) before it can be used. Occasionally transactions get stuck in an '[unconfirmed](https://changelly.com/blog/transaction-stuck-unconfirmed/)' state, which can happen if the mining fee is set too low. Miners work by exchanging a small fee for the processing time it takes to confirm a transaction. The lower the fee, the longer the transaction may stay unconfirmed. This can be avoided by [checking the fee](https://hackernoon.com/holy-cow-i-sent-a-bitcoin-transaction-with-too-low-fees-are-my-coins-lost-forever-7a865e2e45ba) before purchasing.

Once you’ve bought some cryptocurrency, you can follow [this tutorial](https://www.vpnmentor.com/blog/pay-anonymously-ins-outs-anonymous-payment-methods/) to pay for things anonymously. At the very least, use the Tor Browser to mask your location whilst making a purchase.

# Closing Notes
The NSA revelations suggest it’s probably safer to be over-cautious, rather than too relaxed, as ignorance is easy to exploit. However, as there’s no perfect solution, there’s always a tradeoff to be made between paranoia and practicality. 

Nothing beats abstaining from technology, but if you have the time and expertise, hosting open-source solutions on your your own server would be the safest (most private) option.

If you choose third-party solutions, follow them on Twitter, and check their blogs often. Companies (especially smaller ones) often get acquired by larger companies. If the acquisitions seem suspicious, the parent company seems troubling, or the company’s jurisdiction changes, it’s worth finding another provider. If you don't check, these changes might happen invisibly.

# Appendix

## 5 Eyes (avoid)
1. Australia
2. Canada
3. New Zealand
4. United Kingdom
5. United States

## 9 Eyes (try to avoid)
6. Denmark
7. France
8. Netherlands
9. Norway

## 14 Eyes (try to avoid)
10. Germany ([getting worse](https://old.reddit.com/r/tutanota/comments/dwqqzs/tutanota_its_not_safe/))
11. Belgium
12. Italy
13. Sweden
14. Spain

## Useful Websites

- [14 eyes](https://www.privacytools.io/providers/#ukusa)
- [Privacy Tools](https://www.privacytools.io/)
- [Restore Privacy](https://restoreprivacy.com/)
- [PRISM Break](https://prism-break.org/)
- [The complete list of alternative to all Google products](https://www.techspot.com/news/80729-complete-list-alternatives-all-google-products.html)
- [How to restore your privacy huge list](https://www.google.com/url?q=https://www.reddit.com/r/privacytoolsIO/comments/g1z01w/guide_to_how_to_restore_your_privacy_huge_list/&sa=D&source=editors&ust=1613971005610000&usg=AOvVaw03BblmrZ7fLRheNHcjB3uE)
- [Alternatives to google and facebook and reclaiming privacy](https://www.reddit.com/r/dropgoogle/comments/5l0fwj/alternatives_to_google_facebook_and_reclaiming/)
- [List of privacy-conscious email services](https://prxbx.com/email/)
- [Drop Google](https://dropgoogle.com/)
- [Privacy Brochure - A Benchmark Study](https://www.wu.ac.at/ec/projects/privacy-brochure-a-benchmark-study/)
- [εxodus - Android app privacy audit](https://reports.exodus-privacy.eu.org/en/)

The following websites are worth a read, but may not be as accurate:

- [Proprivacy](https://proprivacy.com)
- [Privacy Watchdog](https://privacy-watchdog.io)
- [NSA in Germany](https://www.wsws.org/en/articles/2013/07/11/gspy-j11.html)
