#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import os
from gi.repository.GdkPixbuf import Pixbuf
import platform

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="OBRevenge OS Software Installation Tool")
        self.set_border_width(6)
        self.set_default_size(1200, 700)
        self.main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_box)
        self.titlebox = Gtk.Box()
        self.titlelabel = Gtk.Label()
        self.titlelabel.set_markup("<big>OBRevenge OS Software Installation Tool</big>\nSelect the software that you would like to install and click the 'Install' button.\nApplications may only be installed one at a time.")
        self.mainimage = Gtk.Image()
        self.mainimage.set_size_request(100, 100)
        self.mainimage.set_from_file('/usr/share/Icons/obr-logo-sm.png')
        self.titlebox.pack_start(self.mainimage, True, True, 0)
        self.titlebox.pack_start(self.titlelabel, True, True, 0)
        self.window = Gtk.ScrolledWindow()
        self.window.set_border_width(10)
        self.main_box.pack_start(self.titlebox, False, False, 0)
        self.main_box.pack_start(self.window, True, True, 0)

        self.notebook = Gtk.Notebook()
        self.window.add(self.notebook)

        self.buttonbox = Gtk.Box()
        self.buttonbox.set_spacing(20)
        self.installbutton = Gtk.Button("Install Selected Packages")
        self.installbutton.connect("clicked", self.install)
        self.closebutton = Gtk.Button("Close")
        self.closebutton.connect("clicked", Gtk.main_quit)
        self.buttonbox.pack_end(self.closebutton, False, False, 0)
        self.buttonbox.pack_end(self.installbutton, False, False, 0)
        self.main_box.pack_end(self.buttonbox, False, False, 0)
        # Creating blank package list
        self.packages = []

        # Creating Page 1
        self.page1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page1.set_border_width(10)

        #google-chrome
        self.gchromebox = Gtk.Box(spacing=10)
        self.gchromebox.set_homogeneous(20)
        self.gchromelabel = Gtk.Label("Chromium")
        self.gchromebox.pack_start(self.gchromelabel, True, True, 0)
        # Only packing the google chrome box if it's a 64bit system
        if platform.machine() == 'x86_64':
            self.page1.pack_start(self.gchromebox, True, True, 0)
        self.gchromeimage = Gtk.Image()
        self.gchromeimage.set_from_icon_name('google-chrome', Gtk.IconSize.DIALOG)
        self.gchromebox.pack_start(self.gchromeimage, True, True, 0)
        self.gchromedesc = Gtk.Label("Google's Chrome Browser")
        self.gchromebox.pack_start(self.gchromedesc, True, True, 0)
        self.gchromebutton = Gtk.CheckButton("Install")
        self.gchromebutton.connect("toggled", self.gchrome)
        self.gchromebox.pack_end(self.gchromebutton, False, False, 0)
        #chromium
        self.chromebox = Gtk.Box(spacing=10)
        self.chromebox.set_homogeneous(20)
        self.chromelabel = Gtk.Label("Chromium")
        self.chromebox.pack_start(self.chromelabel, True, True, 0)
        self.page1.pack_start(self.chromebox, True, True, 0)
        self.chromeimage = Gtk.Image()
        self.chromeimage.set_from_icon_name('chromium', Gtk.IconSize.DIALOG)
        self.chromebox.pack_start(self.chromeimage, True, True, 0)
        self.chromedesc = Gtk.Label("Open Source Version of\nGoogle's Chrome Browser")
        self.chromebox.pack_start(self.chromedesc, True, True, 0)
        self.chromebutton = Gtk.CheckButton("Install")
        self.chromebutton.connect("toggled", self.chromium)
        self.chromebox.pack_end(self.chromebutton, False, False, 0)
        #firefox
        self.firebox = Gtk.Box(spacing=10)
        self.firebox.set_homogeneous(20)
        self.firelabel = Gtk.Label("Firefox")
        self.firebox.pack_start(self.firelabel, True, True, 0)
        self.page1.pack_start(self.firebox, True, True, 0)
        self.fireimage = Gtk.Image()
        self.fireimage.set_from_icon_name('firefox', Gtk.IconSize.DIALOG)
        self.firebox.pack_start(self.fireimage, True, True, 0)
        self.firedesc = Gtk.Label("Popular Mozilla Firefox\nWeb Browser")
        self.firebox.pack_start(self.firedesc, True, True, 0)
        self.firebutton = Gtk.CheckButton("Install")
        self.firebutton.connect("clicked", self.firefox)
        self.firebox.pack_end(self.firebutton, False, False, 0)
        #midori
        self.midoribox = Gtk.Box(spacing=10)
        self.midoribox.set_homogeneous(20)
        self.midorilabel = Gtk.Label("Midori")
        self.midoribox.pack_start(self.midorilabel, True, True, 0)
        self.page1.pack_start(self.midoribox, True, True, 0)
        self.midoriimage = Gtk.Image()
        self.midoriimage.set_from_icon_name('midori', Gtk.IconSize.DIALOG)
        self.midoribox.pack_start(self.midoriimage, True, True, 0)
        self.midoridesc = Gtk.Label("Popular Open Source Browser")
        self.midoribox.pack_start(self.midoridesc, True, True, 0)
        self.midoributton = Gtk.CheckButton("Install")
        self.midoributton.connect("clicked", self.midori)
        self.midoribox.pack_end(self.midoributton, False, False, 0)
        #qupzila
        self.qupbox = Gtk.Box(spacing=10)
        self.qupbox.set_homogeneous(20)
        self.quplabel = Gtk.Label("Qupzilla")
        self.qupbox.pack_start(self.quplabel, True, True, 0)
        self.page1.pack_start(self.qupbox, True, True, 0)
        self.qupimage = Gtk.Image()
        self.qupimage.set_from_icon_name('qupzilla', Gtk.IconSize.DIALOG)
        self.qupbox.pack_start(self.qupimage, True, True, 0)
        self.qupdesc = Gtk.Label("Popular Open Source Browser\nBased on QT")
        self.qupbox.pack_start(self.qupdesc, True, True, 0)
        self.qupbutton = Gtk.CheckButton("Install")
        self.qupbutton.connect("clicked", self.qupzilla)
        self.qupbox.pack_end(self.qupbutton, False, False, 0)
        #netsurf
        self.netbox = Gtk.Box(spacing=10)
        self.netbox.set_homogeneous(20)
        self.netlabel = Gtk.Label("Netsurf")
        self.netbox.pack_start(self.netlabel, True, True, 0)
        self.page1.pack_start(self.netbox, True, True, 0)
        self.netimage = Gtk.Image()
        self.netimage.set_from_icon_name('netsurf', Gtk.IconSize.DIALOG)
        self.netbox.pack_start(self.netimage, True, True, 0)
        self.netdesc = Gtk.Label("Lightweight Open Source Browser")
        self.netbox.pack_start(self.netdesc, True, True, 0)
        self.netbutton = Gtk.CheckButton("Install")
        self.netbutton.connect("clicked", self.netsurf)
        self.netbox.pack_end(self.netbutton, False, False, 0)
        #filezilla
        self.filbox = Gtk.Box(spacing=10)
        self.filbox.set_homogeneous(20)
        self.fillabel = Gtk.Label("Filezilla")
        self.filbox.pack_start(self.fillabel, True, True, 0)
        self.page1.pack_start(self.filbox, True, True, 0)
        self.filimage = Gtk.Image()
        self.filimage.set_from_icon_name('filezilla', Gtk.IconSize.DIALOG)
        self.filbox.pack_start(self.filimage, True, True, 0)
        self.fildesc = Gtk.Label("Graphical SSH Tool")
        self.filbox.pack_start(self.fildesc, True, True, 0)
        self.filbutton = Gtk.CheckButton("Install")
        self.filbutton.connect("clicked", self.filezilla)
        self.filbox.pack_end(self.filbutton, False, False, 0)
        #opera
        self.opebox = Gtk.Box(spacing=10)
        self.opebox.set_homogeneous(20)
        self.opelabel = Gtk.Label("Opera")
        self.opebox.pack_start(self.opelabel, True, True, 0)
        self.page1.pack_start(self.opebox, True, True, 0)
        self.opeimage = Gtk.Image()
        self.opeimage.set_from_icon_name('opera', Gtk.IconSize.DIALOG)
        self.opebox.pack_start(self.opeimage, True, True, 0)
        self.opedesc = Gtk.Label("Popular Opera Open Source Browser")
        self.opebox.pack_start(self.opedesc, True, True, 0)
        self.opebutton = Gtk.CheckButton("Install")
        self.opebutton.connect("clicked", self.opera)
        self.opebox.pack_end(self.opebutton, False, False, 0)
        #geary
        self.geabox = Gtk.Box(spacing=10)
        self.geabox.set_homogeneous(20)
        self.gealabel = Gtk.Label("Geary")
        self.geabox.pack_start(self.gealabel, True, True, 0)
        self.page1.pack_start(self.geabox, True, True, 0)
        self.geaimage = Gtk.Image()
        self.geaimage.set_from_icon_name('geary', Gtk.IconSize.DIALOG)
        self.geabox.pack_start(self.geaimage, True, True, 0)
        self.geadesc = Gtk.Label("Open Source GTK Email Client")
        self.geabox.pack_start(self.geadesc, True, True, 0)
        self.geabutton = Gtk.CheckButton("Install")
        self.geabutton.connect("clicked", self.geary)
        self.geabox.pack_end(self.geabutton, False, False, 0)
        #evolution
        self.evobox = Gtk.Box(spacing=10)
        self.evobox.set_homogeneous(20)
        self.evolabel = Gtk.Label("Evolution")
        self.evobox.pack_start(self.evolabel, True, True, 0)
        self.page1.pack_start(self.evobox, True, True, 0)
        self.evoimage = Gtk.Image()
        self.evoimage.set_from_icon_name('evolution', Gtk.IconSize.DIALOG)
        self.evobox.pack_start(self.evoimage, True, True, 0)
        self.evodesc = Gtk.Label("Open Source Email client")
        self.evobox.pack_start(self.evodesc, True, True, 0)
        self.evobutton = Gtk.CheckButton("Install")
        self.evobutton.connect("clicked", self.evolution)
        self.evobox.pack_end(self.evobutton, False, False, 0)
        #thunderbird
        self.thubox = Gtk.Box(spacing=10)
        self.thubox.set_homogeneous(20)
        self.thulabel = Gtk.Label("Thunderbird")
        self.thubox.pack_start(self.thulabel, True, True, 0)
        self.page1.pack_start(self.thubox, True, True, 0)
        self.thuimage = Gtk.Image()
        self.thuimage.set_from_icon_name('thunderbird', Gtk.IconSize.DIALOG)
        self.thubox.pack_start(self.thuimage, True, True, 0)
        self.thudesc = Gtk.Label("Mozilla's Open Source\nEmail Client'")
        self.thubox.pack_start(self.thudesc, True, True, 0)
        self.thubutton = Gtk.CheckButton("Install")
        self.thubutton.connect("clicked", self.thunderbird)
        self.thubox.pack_end(self.thubutton, False, False, 0)
        #transmission
        self.trabox = Gtk.Box(spacing=10)
        self.trabox.set_homogeneous(20)
        self.tralabel = Gtk.Label("Transmission")
        self.trabox.pack_start(self.tralabel, True, True, 0)
        self.page1.pack_start(self.trabox, True, True, 0)
        self.traimage = Gtk.Image()
        self.traimage.set_from_icon_name('transmission-gtk', Gtk.IconSize.DIALOG)
        self.trabox.pack_start(self.traimage, True, True, 0)
        self.tradesc = Gtk.Label("Popular GTK Torrent\nDownload Tool")
        self.trabox.pack_start(self.tradesc, True, True, 0)
        self.trabutton = Gtk.CheckButton("Install")
        self.trabutton.connect("clicked", self.transmission)
        self.trabox.pack_end(self.trabutton, False, False, 0)
        #qbittorrent
        self.qbibox = Gtk.Box(spacing=10)
        self.qbibox.set_homogeneous(20)
        self.qbilabel = Gtk.Label("QBittorrent")
        self.qbibox.pack_start(self.qbilabel, True, True, 0)
        self.page1.pack_start(self.qbibox, True, True, 0)
        self.qbiimage = Gtk.Image()
        self.qbiimage.set_from_icon_name('qbittorrent', Gtk.IconSize.DIALOG)
        self.qbibox.pack_start(self.qbiimage, True, True, 0)
        self.qbidesc = Gtk.Label("QT Based Bit Torrent Client")
        self.qbibox.pack_start(self.qbidesc, True, True, 0)
        self.qbibutton = Gtk.CheckButton("Install")
        self.qbibutton.connect("clicked", self.qbittorrent)
        self.qbibox.pack_end(self.qbibutton, False, False, 0)
        #hexchat
        self.hexbox = Gtk.Box(spacing=10)
        self.hexbox.set_homogeneous(20)
        self.hexlabel = Gtk.Label("Hexchat")
        self.hexbox.pack_start(self.hexlabel, True, True, 0)
        self.page1.pack_start(self.hexbox, True, True, 0)
        self.heximage = Gtk.Image()
        self.heximage.set_from_icon_name('hexchat', Gtk.IconSize.DIALOG)
        self.hexbox.pack_start(self.heximage, True, True, 0)
        self.hexdesc = Gtk.Label("Popular Multi-Platform\nChat Client")
        self.hexbox.pack_start(self.hexdesc, True, True, 0)
        self.hexbutton = Gtk.CheckButton("Install")
        self.hexbutton.connect("clicked", self.hexchat)
        self.hexbox.pack_end(self.hexbutton, False, False, 0)
        # adding page 1
        self.notebook.append_page(self.page1, Gtk.Label('Internet'))

        # Creating Page 2
        self.page2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page2.set_border_width(10)

        #gimp
        self.gimpbox = Gtk.Box(spacing=10)
        self.gimpbox.set_homogeneous(20)
        self.gimplabel = Gtk.Label("Gimp")
        self.gimpbox.pack_start(self.gimplabel, True, True, 0)
        self.page2.pack_start(self.gimpbox, True, True, 0)
        self.gimpimage = Gtk.Image()
        self.gimpimage.set_from_icon_name('gimp', Gtk.IconSize.DIALOG)
        self.gimpbox.pack_start(self.gimpimage, True, True, 0)
        self.gimpdesc = Gtk.Label("Powerful Open Source\nImage Manipulation Program")
        self.gimpbox.pack_start(self.gimpdesc, True, True, 0)
        self.gimpbutton = Gtk.CheckButton("Install")
        self.gimpbutton.connect("toggled", self.gimp)
        self.gimpbox.pack_end(self.gimpbutton, False, False, 0)
        #vlc
        self.vlcbox = Gtk.Box(spacing=10)
        self.vlcbox.set_homogeneous(20)
        self.vlclabel = Gtk.Label("VLC")
        self.vlcbox.pack_start(self.vlclabel, True, True, 0)
        self.page2.pack_start(self.vlcbox, True, True, 0)
        self.vlcimage = Gtk.Image()
        self.vlcimage.set_from_icon_name('vlc', Gtk.IconSize.DIALOG)
        self.vlcbox.pack_start(self.vlcimage, True, True, 0)
        self.vlcdesc = Gtk.Label("Popular Open Source\nMultimedia Player")
        self.vlcbox.pack_start(self.vlcdesc, True, True, 0)
        self.vlcbutton = Gtk.CheckButton("Install")
        self.vlcbutton.connect("clicked", self.vlc)
        self.vlcbox.pack_end(self.vlcbutton, False, False, 0)
        #totem
        self.totembox = Gtk.Box(spacing=10)
        self.totembox.set_homogeneous(20)
        self.totemlabel = Gtk.Label("Totem")
        self.totembox.pack_start(self.totemlabel, True, True, 0)
        self.page2.pack_start(self.totembox, True, True, 0)
        self.totemimage = Gtk.Image()
        self.totemimage.set_from_icon_name('totem', Gtk.IconSize.DIALOG)
        self.totembox.pack_start(self.totemimage, True, True, 0)
        self.totemdesc = Gtk.Label("Popular Open Source Browser")
        self.totembox.pack_start(self.totemdesc, True, True, 0)
        self.totembutton = Gtk.CheckButton("Install")
        self.totembutton.connect("clicked", self.totem)
        self.totembox.pack_end(self.totembutton, False, False, 0)
        #qupzila
        self.parbox = Gtk.Box(spacing=10)
        self.parbox.set_homogeneous(20)
        self.parlabel = Gtk.Label("Parole")
        self.parbox.pack_start(self.parlabel, True, True, 0)
        self.page2.pack_start(self.parbox, True, True, 0)
        self.parimage = Gtk.Image()
        self.parimage.set_from_icon_name('parole', Gtk.IconSize.DIALOG)
        self.parbox.pack_start(self.parimage, True, True, 0)
        self.pardesc = Gtk.Label("Popular Open Source\nMedia Player")
        self.parbox.pack_start(self.pardesc, True, True, 0)
        self.parbutton = Gtk.CheckButton("Install")
        self.parbutton.connect("clicked", self.parole)
        self.parbox.pack_end(self.parbutton, False, False, 0)
        #spotify
        self.spotbox = Gtk.Box(spacing=10)
        self.spotbox.set_homogeneous(20)
        self.spotlabel = Gtk.Label("Spotify")
        self.spotbox.pack_start(self.spotlabel, True, True, 0)
        self.page2.pack_start(self.spotbox, True, True, 0)
        self.spotimage = Gtk.Image()
        self.spotimage.set_from_icon_name('spotify', Gtk.IconSize.DIALOG)
        self.spotbox.pack_start(self.spotimage, True, True, 0)
        self.spotdesc = Gtk.Label("Music Streaming Service Application")
        self.spotbox.pack_start(self.spotdesc, True, True, 0)
        self.spotbutton = Gtk.CheckButton("Install")
        self.spotbutton.connect("clicked", self.spotify)
        self.spotbox.pack_end(self.spotbutton, False, False, 0)
        #audacious
        self.audbox = Gtk.Box(spacing=10)
        self.audbox.set_homogeneous(20)
        self.audlabel = Gtk.Label("Audacious")
        self.audbox.pack_start(self.audlabel, True, True, 0)
        self.page2.pack_start(self.audbox, True, True, 0)
        self.audimage = Gtk.Image()
        self.audimage.set_from_icon_name('audacious', Gtk.IconSize.DIALOG)
        self.audbox.pack_start(self.audimage, True, True, 0)
        self.auddesc = Gtk.Label("Popular music player and Utility")
        self.audbox.pack_start(self.auddesc, True, True, 0)
        self.audbutton = Gtk.CheckButton("Install")
        self.audbutton.connect("clicked", self.audacious)
        self.audbox.pack_end(self.audbutton, False, False, 0)
        #clementine
        self.clebox = Gtk.Box(spacing=10)
        self.clebox.set_homogeneous(20)
        self.clelabel = Gtk.Label("Clementine")
        self.clebox.pack_start(self.clelabel, True, True, 0)
        self.page2.pack_start(self.clebox, True, True, 0)
        self.cleimage = Gtk.Image()
        self.cleimage.set_from_icon_name('clementine', Gtk.IconSize.DIALOG)
        self.clebox.pack_start(self.cleimage, True, True, 0)
        self.cledesc = Gtk.Label("Popular GTK Music Player\nAnd Music Utility")
        self.clebox.pack_start(self.cledesc, True, True, 0)
        self.clebutton = Gtk.CheckButton("Install")
        self.clebutton.connect("clicked", self.clementine)
        self.clebox.pack_end(self.clebutton, False, False, 0)
        #gthumb
        self.gthbox = Gtk.Box(spacing=10)
        self.gthbox.set_homogeneous(20)
        self.gthlabel = Gtk.Label("Gthumb")
        self.gthbox.pack_start(self.gthlabel, True, True, 0)
        self.page2.pack_start(self.gthbox, True, True, 0)
        self.gthimage = Gtk.Image()
        self.gthimage.set_from_icon_name('gthumb', Gtk.IconSize.DIALOG)
        self.gthbox.pack_start(self.gthimage, True, True, 0)
        self.gthdesc = Gtk.Label("Popular GTK Image Viewer\nAnd Image Utility")
        self.gthbox.pack_start(self.gthdesc, True, True, 0)
        self.gthbutton = Gtk.CheckButton("Install")
        self.gthbutton.connect("clicked", self.gthumb)
        self.gthbox.pack_end(self.gthbutton, False, False, 0)
        #shotwell
        self.shobox = Gtk.Box(spacing=10)
        self.shobox.set_homogeneous(20)
        self.sholabel = Gtk.Label("Shotwell")
        self.shobox.pack_start(self.sholabel, True, True, 0)
        self.page2.pack_start(self.shobox, True, True, 0)
        self.shoimage = Gtk.Image()
        self.shoimage.set_from_icon_name('shotwell', Gtk.IconSize.DIALOG)
        self.shobox.pack_start(self.shoimage, True, True, 0)
        self.shodesc = Gtk.Label("Image Utility and Viewer")
        self.shobox.pack_start(self.shodesc, True, True, 0)
        self.shobutton = Gtk.CheckButton("Install")
        self.shobutton.connect("clicked", self.shotwell)
        self.shobox.pack_end(self.shobutton, False, False, 0)
        #ristretto
        self.risbox = Gtk.Box(spacing=10)
        self.risbox.set_homogeneous(20)
        self.rislabel = Gtk.Label("Ristretto")
        self.risbox.pack_start(self.rislabel, True, True, 0)
        self.page2.pack_start(self.risbox, True, True, 0)
        self.risimage = Gtk.Image()
        self.risimage.set_from_icon_name('ristretto', Gtk.IconSize.DIALOG)
        self.risbox.pack_start(self.risimage, True, True, 0)
        self.risdesc = Gtk.Label("Music Utility and Player")
        self.risbox.pack_start(self.risdesc, True, True, 0)
        self.risbutton = Gtk.CheckButton("Install")
        self.risbutton.connect("clicked", self.ristretto)
        self.risbox.pack_end(self.risbutton, False, False, 0)
        #gpicview
        self.gpibox = Gtk.Box(spacing=10)
        self.gpibox.set_homogeneous(20)
        self.gpilabel = Gtk.Label("Gpicview")
        self.gpibox.pack_start(self.gpilabel, True, True, 0)
        self.page2.pack_start(self.gpibox, True, True, 0)
        self.gpiimage = Gtk.Image()
        self.gpiimage.set_from_icon_name('gpicview', Gtk.IconSize.DIALOG)
        self.gpibox.pack_start(self.gpiimage, True, True, 0)
        self.gpidesc = Gtk.Label("GTK Photo Manager and Viewer")
        self.gpibox.pack_start(self.gpidesc, True, True, 0)
        self.gpibutton = Gtk.CheckButton("Install")
        self.gpibutton.connect("clicked", self.gpicview)
        self.gpibox.pack_end(self.gpibutton, False, False, 0)
        #audicity
        self.adybox = Gtk.Box(spacing=10)
        self.adybox.set_homogeneous(20)
        self.adylabel = Gtk.Label("Audicity")
        self.adybox.pack_start(self.adylabel, True, True, 0)
        self.page2.pack_start(self.adybox, True, True, 0)
        self.adyimage = Gtk.Image()
        self.adyimage.set_from_icon_name('audacity', Gtk.IconSize.DIALOG)
        self.adybox.pack_start(self.adyimage, True, True, 0)
        self.adydesc = Gtk.Label("Music File Configuration Tool")
        self.adybox.pack_start(self.adydesc, True, True, 0)
        self.adybutton = Gtk.CheckButton("Install")
        self.adybutton.connect("clicked", self.audicity)
        self.adybox.pack_end(self.adybutton, False, False, 0)
        #ssr
        self.ssrbox = Gtk.Box(spacing=10)
        self.ssrbox.set_homogeneous(20)
        self.ssrlabel = Gtk.Label("Simple Screen Recorder")
        self.ssrbox.pack_start(self.ssrlabel, True, True, 0)
        self.page2.pack_start(self.ssrbox, True, True, 0)
        self.ssrimage = Gtk.Image()
        self.ssrimage.set_from_icon_name('hexchat', Gtk.IconSize.DIALOG)
        self.ssrbox.pack_start(self.ssrimage, True, True, 0)
        self.ssrdesc = Gtk.Label("Excellent Screen Capturing Software")
        self.ssrbox.pack_start(self.ssrdesc, True, True, 0)
        self.ssrbutton = Gtk.CheckButton("Install")
        self.ssrbutton.connect("clicked", self.ssr)
        self.ssrbox.pack_end(self.ssrbutton, False, False, 0)
        #kdenlive
        self.kdebox = Gtk.Box(spacing=10)
        self.kdebox.set_homogeneous(20)
        self.kdelabel = Gtk.Label("Kdenlive")
        self.kdebox.pack_start(self.kdelabel, True, True, 0)
        self.page2.pack_start(self.kdebox, True, True, 0)
        self.kdeimage = Gtk.Image()
        self.kdeimage.set_from_icon_name('kdenlive', Gtk.IconSize.DIALOG)
        self.kdebox.pack_start(self.kdeimage, True, True, 0)
        self.kdedesc = Gtk.Label("Excellent Video Editing Software")
        self.kdebox.pack_start(self.kdedesc, True, True, 0)
        self.kdebutton = Gtk.CheckButton("Install")
        self.kdebutton.connect("clicked", self.kde)
        self.kdebox.pack_end(self.kdebutton, False, False, 0)
        #obs-studio
        self.obsbox = Gtk.Box(spacing=10)
        self.obsbox.set_homogeneous(20)
        self.obslabel = Gtk.Label("OBS-Studio")
        self.obsbox.pack_start(self.obslabel, True, True, 0)
        self.page2.pack_start(self.obsbox, True, True, 0)
        self.obsimage = Gtk.Image()
        self.obsimage.set_from_icon_name('obs', Gtk.IconSize.DIALOG)
        self.obsbox.pack_start(self.obsimage, True, True, 0)
        self.obsdesc = Gtk.Label("Screen Capturing and Streaming Software")
        self.obsbox.pack_start(self.obsdesc, True, True, 0)
        self.obsbutton = Gtk.CheckButton("Install")
        self.obsbutton.connect("clicked", self.obs)
        self.obsbox.pack_end(self.obsbutton, False, False, 0)
        # adding page 2
        self.notebook.append_page(self.page2, Gtk.Label('Media'))
        
        # Creating Page 3
        self.page3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.page2.set_border_width(10)

        #libreoffice
        self.libpbox = Gtk.Box(spacing=10)
        self.libpbox.set_homogeneous(20)
        self.libplabel = Gtk.Label("Libre Office (Fresh)")
        self.libpbox.pack_start(self.libplabel, True, True, 0)
        self.page3.pack_start(self.libpbox, False, False, 0)
        self.libpimage = Gtk.Image()
        self.libpimage.set_from_icon_name('libreoffice', Gtk.IconSize.DIALOG)
        self.libpbox.pack_start(self.libpimage, True, True, 0)
        self.libpdesc = Gtk.Label("Powerful Open Source Office Suite")
        self.libpbox.pack_start(self.libpdesc, True, True, 0)
        self.libpbutton = Gtk.CheckButton("Install")
        self.libpbutton.connect("toggled", self.libre)
        self.libpbox.pack_end(self.libpbutton, False, False, 0)
        #calligra
        self.calbox = Gtk.Box(spacing=10)
        self.calbox.set_homogeneous(20)
        self.callabel = Gtk.Label("Calligra Office")
        self.calbox.pack_start(self.callabel, True, True, 0)
        self.page3.pack_start(self.calbox, False, False, 0)
        self.calimage = Gtk.Image()
        self.calimage.set_from_icon_name('calligrawords', Gtk.IconSize.DIALOG)
        self.calbox.pack_start(self.calimage, True, True, 0)
        self.caldesc = Gtk.Label("QT Based Office Suite")
        self.calbox.pack_start(self.caldesc, True, True, 0)
        self.calbutton = Gtk.CheckButton("Install")
        self.calbutton.connect("clicked", self.calligra)
        self.calbox.pack_end(self.calbutton, False, False, 0)
        #abiword
        self.abibox = Gtk.Box(spacing=10)
        self.abibox.set_homogeneous(20)
        self.abilabel = Gtk.Label("Abiword")
        self.abibox.pack_start(self.abilabel, True, True, 0)
        self.page3.pack_start(self.abibox, False, False, 0)
        self.abiimage = Gtk.Image()
        self.abiimage.set_from_icon_name('abiword', Gtk.IconSize.DIALOG)
        self.abibox.pack_start(self.abiimage, True, True, 0)
        self.abidesc = Gtk.Label("Lightweight Word Processor")
        self.abibox.pack_start(self.abidesc, True, True, 0)
        self.abibutton = Gtk.CheckButton("Install")
        self.abibutton.connect("clicked", self.abiword)
        self.abibox.pack_end(self.abibutton, False, False, 0)
        #gnumeric
        self.gnubox = Gtk.Box(spacing=10)
        self.gnubox.set_homogeneous(20)
        self.gnulabel = Gtk.Label("Gnumeric")
        self.gnubox.pack_start(self.gnulabel, True, True, 0)
        self.page3.pack_start(self.gnubox, False, False, 0)
        self.gnuimage = Gtk.Image()
        self.gnuimage.set_from_icon_name('gnumeric', Gtk.IconSize.DIALOG)
        self.gnubox.pack_start(self.gnuimage, True, True, 0)
        self.gnudesc = Gtk.Label("Lightweight Spreadsheet Program")
        self.gnubox.pack_start(self.gnudesc, True, True, 0)
        self.gnubutton = Gtk.CheckButton("Install")
        self.gnubutton.connect("clicked", self.gnumeric)
        self.gnubox.pack_end(self.gnubutton, False, False, 0)
        #pdfmod
        self.pdfbox = Gtk.Box(spacing=10)
        self.pdfbox.set_homogeneous(20)
        self.pdflabel = Gtk.Label("PDFMod")
        self.pdfbox.pack_start(self.pdflabel, True, True, 0)
        self.page3.pack_start(self.pdfbox, False, False, 0)
        self.pdfimage = Gtk.Image()
        self.pdfimage.set_from_icon_name('pdfmod', Gtk.IconSize.DIALOG)
        self.pdfbox.pack_start(self.pdfimage, True, True, 0)
        self.pdfdesc = Gtk.Label("Powerful PDF Managment Software")
        self.pdfbox.pack_start(self.pdfdesc, True, True, 0)
        self.pdfbutton = Gtk.CheckButton("Install")
        self.pdfbutton.connect("clicked", self.pdfmod)
        self.pdfbox.pack_end(self.pdfbutton, False, False, 0)
        #evince
        self.evibox = Gtk.Box(spacing=10)
        self.evibox.set_homogeneous(20)
        self.evilabel = Gtk.Label("Evince")
        self.evibox.pack_start(self.evilabel, True, True, 0)
        self.page3.pack_start(self.evibox, False, False, 0)
        self.eviimage = Gtk.Image()
        self.eviimage.set_from_icon_name('evince', Gtk.IconSize.DIALOG)
        self.evibox.pack_start(self.eviimage, True, True, 0)
        self.evidesc = Gtk.Label("Simple PDF Viewer")
        self.evibox.pack_start(self.evidesc, True, True, 0)
        self.evibutton = Gtk.CheckButton("Install")
        self.evibutton.connect("clicked", self.evince)
        self.evibox.pack_end(self.evibutton, False, False, 0)
        #calibre
        self.calbox = Gtk.Box(spacing=10)
        self.calbox.set_homogeneous(20)
        self.callabel = Gtk.Label("Calibre")
        self.calbox.pack_start(self.callabel, True, True, 0)
        self.page3.pack_start(self.calbox, False, False, 0)
        self.calimage = Gtk.Image()
        self.calimage.set_from_icon_name('calibre', Gtk.IconSize.DIALOG)
        self.calbox.pack_start(self.calimage, True, True, 0)
        self.caldesc = Gtk.Label("Popular E-Book Reader for the Desktop\nQT Based")
        self.calbox.pack_start(self.caldesc, True, True, 0)
        self.calbutton = Gtk.CheckButton("Install")
        self.calbutton.connect("clicked", self.calibre)
        self.calbox.pack_end(self.calbutton, False, False, 0)
        #fbreader
        self.fbrbox = Gtk.Box(spacing=10)
        self.fbrbox.set_homogeneous(20)
        self.fbrlabel = Gtk.Label("FBReader")
        self.fbrbox.pack_start(self.fbrlabel, True, True, 0)
        self.page3.pack_start(self.fbrbox, False, False, 0)
        self.fbrimage = Gtk.Image()
        self.fbrimage.set_from_icon_name('fbreader', Gtk.IconSize.DIALOG)
        self.fbrbox.pack_start(self.fbrimage, True, True, 0)
        self.fbrdesc = Gtk.Label("Popular E-Book Reader for the Desktop\nGTK Based")
        self.fbrbox.pack_start(self.fbrdesc, True, True, 0)
        self.fbrbutton = Gtk.CheckButton("Install")
        self.fbrbutton.connect("clicked", self.fbreader)
        self.fbrbox.pack_end(self.fbrbutton, False, False, 0)
        # adding page 3
        self.notebook.append_page(self.page3, Gtk.Label('Office'))


    def chromium(self, widget):
        if self.chromebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('chromium')
        else:
            self.packages.remove('chromium')
        print(self.packages)
        
    def gchrome(self, widget):
        if self.gchromebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('google-chrome')
        else:
            self.packages.remove('google-chrome')
        print(self.packages)

    def firefox(self, widget):
        if self.firebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('firefox')
        else:
            self.packages.remove('firefox')
        print(self.packages)

    def midori(self, widget):
        if self.midoributton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('midori')
        else:
            self.packages.remove('midori')
        print(self.packages)

    def qupzilla(self, widget):
        if self.qupbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('qupzilla')
        else:
            self.packages.remove('qupzilla')
        print(self.packages)

    def netsurf(self, widget):
        if self.netbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('netsurf')
        else:
            self.packages.remove('netsurf')
        print(self.packages)

    def filezilla(self, widget):
        if self.filbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('filezilla')
        else:
            self.packages.remove('filezilla')
        print(self.packages)

    def opera(self, widget):
        if self.opebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('opera')
        else:
            self.packages.remove('opera')
        print(self.packages)

    def geary(self, widget):
        if self.geabutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('geary')
        else:
            self.packages.remove('geary')
        print(self.packages)

    def evolution(self, widget):
        if self.evobutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('evolution')
        else:
            self.packages.remove('evolution')
        print(self.packages)

    def thunderbird(self, widget):
        if self.thubutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('thunderbird')
        else:
            self.packages.remove('thunderbird')
        print(self.packages)

    def transmission(self, widget):
        if self.trabutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('transmission-gtk')
        else:
            self.packages.remove('transmission-gtk')
        print(self.packages)

    def qbittorrent(self, widget):
        if self.qbibutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('qbittorrent')
        else:
            self.packages.remove('qbittorrent')
        print(self.packages)

    def hexchat(self, widget):
        if self.hexbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('hexchat')
        else:
            self.packages.remove('hexchat')
        print(self.packages)
        
    def gimp(self, widget):
        if self.gimpbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('gimp')
        else:
            self.packages.remove('gimp')
        print(self.packages)
    
    def vlc(self, widget):
        if self.vlcbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('vlc')
        else:
            self.packages.remove('vlc')
        print(self.packages)
        
    def totem(self, widget):
        if self.totembutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('totem')
        else:
            self.packages.remove('totem')
        print(self.packages)
        
    def spotify(self, widget):
        if self.spotbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('spotify')
        else:
            self.packages.remove('spotify')
        print(self.packages)
        
    def parole(self, widget):
        if self.parbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('parole')
        else:
            self.packages.remove('parole')
        print(self.packages)
        
    def audacious(self, widget):
        if self.audbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('audacious')
        else:
            self.packages.remove('audacious')
        print(self.packages)
        
    def clementine(self, widget):
        if self.clebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('clementine')
        else:
            self.packages.remove('clementine')
        print(self.packages)
        
    def gthumb(self, widget):
        if self.gthbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('gthumb')
        else:
            self.packages.remove('gthumb')
        print(self.packages)
        
    def shotwell(self, widget):
        if self.shobutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('shotwell')
        else:
            self.packages.remove('shotwell')
        print(self.packages)
        
    def ristretto(self, widget):
        if self.risbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('ristretto')
        else:
            self.packages.remove('ristretto')
        print(self.packages)
        
    def gpicview(self, widget):
        if self.gpibutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('gpicview')
        else:
            self.packages.remove('gpicview')
        print(self.packages)
        
    def audicity(self, widget):
        if self.adybutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('audacity')
        else:
            self.packages.remove('audacity')
        print(self.packages)
    
    def ssr(self, widget):
        if self.ssrbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('simplescreenrecorder')
        else:
            self.packages.remove('simplescreenrecorder')
        print(self.packages)
        
    def kde(self, widget):
        if self.kdebutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('kdenlive')
            self.packages.append('breeze-icons')
            self.packages.append('frei0r-plugins')
        else:
            self.packages.remove('breeze-icons')
            self.packages.remove('frei0r-plugins')
            self.packages.remove('kdenlive')
        print(self.packages)
        
    def obs(self, widget):
        if self.obsbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('obs-studio')
        else:
            self.packages.remove('obs-studio')
        print(self.packages)
        
    def libre(self, widget):
        if self.libpbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('libreoffice-fresh')
        else:
            self.packages.remove('libreoffice-fresh')
        print(self.packages)
        
    def calligra(self, widget):
        if self.calbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('calligra')
        else:
            self.packages.remove('calligra')
        print(self.packages)
        
    def abiword(self, widget):
        if self.abibutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('abiword')
        else:
            self.packages.remove('abiword')
        print(self.packages)
        
    def gnumeric(self, widget):
        if self.gnubutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('gnumeric')
        else:
            self.packages.remove('gnumeric')
        print(self.packages)
        
    def pdfmod(self, widget):
        if self.pdfbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('pdfmod')
        else:
            self.packages.remove('pdfmod')
        print(self.packages)
        
    def evince(self, widget):
        if self.evibutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('evince')
        else:
            self.packages.remove('evince')
        print(self.packages)
        
    def calibre(self, widget):
        if self.calbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('calibre')
        else:
            self.packages.remove('calibre')
        print(self.packages)
        
    def fbreader(self, widget):
        if self.fbrbutton.get_active():
            state = "on"
        else:
            state = "off"
        if state is 'on':
            self.packages.append('fbreader')
        else:
            self.packages.remove('fbreader')
        print(self.packages)



    def install(self, widget):
        file = open('.packages.txt', 'w')
        for i in self.packages:
            file.write(i + " ")
        file.close()
        os.system("gksu installapps.sh")



win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
