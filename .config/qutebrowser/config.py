import mountain.draw

# Load existing settings made via :set
config.load_autoconfig()

# Konda means mountain in telugu :P
# Don't worry, I know it's a bad joke too...
mountain.draw.konda(c, {
    'spacing': {
        'vertical': 6,
        'horizontal': 8
    }
})

c.fonts.hints = '11pt Roboto'
c.fonts.keyhint = '11pt Roboto'
c.fonts.prompts = '11pt Roboto'
c.fonts.downloads = '11pt Roboto'
c.fonts.statusbar = '11pt Roboto'
c.fonts.contextmenu = '11pt Roboto'
c.fonts.messages.info = '11pt Roboto'
c.fonts.debug_console = '11pt Roboto'
c.fonts.completion.entry = '11pt Roboto'
c.fonts.completion.category = '11pt Roboto'
c.url.start_pages = "~/.config/qutebrowser/startpage/index.html"
c.url.default_page = "~/.config/qutebrowser/startpage/index.html"
c.editor.command = ['/usr/bin/nvim', '-f', '{}']
