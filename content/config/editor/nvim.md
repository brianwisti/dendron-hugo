---
created: '2024-02-10 05:28:46'
description: ''
fname: pub.config.editor.nvim
id: qqo8xydm0oq8xmbonejuk9d
title: Nvim
updated: '2024-08-25 17:50:32'
---

All right, here goes.

## `init.lua`

A snapshot of my [Neovim]({{< relref "/card/neovim.md" >}}) config, literate programming style.

Right now, everything goes in `init.lua`. I may tidy that up later.

### `init.lua` global prep

Most Neovim Lua functionality is contained in the `vim` module. Pull some of
the frequently used ones into the current namespace, to save a little typing
for our fingers.

`vim.cmd`
: vim commands (eg `cmd('pwd')`)

`vim.fn`
: vim functions (eg `fn.buffer()`)

`vim.g`
: a table for global variables

`vim.opt`
: vim options

```lua
local cmd = vim.cmd
local fn = vim.fn
local g = vim.g
local opt = vim.opt
```

### Helper functions

There's just `map` for the moment.
It creates mappings with `noremap` option enabled by default.

```lua
local function map(mode, lhs, rhs, opts)
  local options = {noremap = true}

  if opts then options = vim.tbl_extend('force', options, opts) end
  vim.api.nvim_set_keymap(mode, lhs, rhs, options)
end
```

### Bootstrap `packer.nvim`

Make sure the [Packer](https://github.com/wbthomason/packer.nvim) plugin manager is instealled and ready.

```lua
local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'

if fn.empty(fn.glob(install_path)) > 0 then
  packer_bootstrap = fn.system({
    'git',
    'clone',
    '--depth', '1',
    'https://github.com/wbthomason/packer.nvim',
    install_path
  })
end

require('packer').startup(function(use)
  use "wbthomason/packer.nvim"

  // ==> Specify my packages.

  if packer_bootstrap then
    require('packer').sync()
  end
end)
```

### The Packages

It's mostly `use "source/repo"`.
I'll pull the more interesting bits out into their own blocks.

```lua
//- Specify my packages

use "nvim-lua/popup.nvim"
use "nvim-lua/plenary.nvim"
use "kyazdani42/nvim-web-devicons"
use "neovim/nvim-lspconfig"

use "EdenEast/nightfox.nvim"
use "RRethy/nvim-base16"
use { "catppuccin/nvim", as = "catpuccin" }
use 'folke/tokyonight.nvim'
use {
  'meliora-theme/neovim',
  requires = {'rktjmp/lush.nvim'},
}
use 'pineapplegiant/spaceduck'

// ==> Load treesitter.
// ==> Load filetype.nvim.
// ==> Load telescope.nvim.
// ==> Load null-ls.nvim.
// ==> Load which-key.nvim.
// ==> Load lualine.nvim.
// ==> Load programming language support.
// ==> Load riv.vim.
```

#### Treesitter

[`nvim-treesitter`](https://github.com/nvim-treesitter/nvim-treesitter) is an experimental binding for Neovim. Something to do with syntax highlighting? Both it and the plugins that use it change frequently. So I better follow the instructions about keeping everything up to date when I sync.

```lua
//- Load treesitter
use {
  "nvim-treesitter/nvim-treesitter",
  run = ":TSUpdate",
  config = function()
    require("nvim-treesitter.configs").setup {
      ensure_installed = "all",
      highlight = {
        enable = true,
      },
      additional_vim_regex_highlighting = false,
    }

    local parser_config = require("nvim-treesitter.parsers").get_parser_configs()
    parser_config.just = {
      install_info = {
        url = "https://github.com/IndianBoy42/tree-sitter-just", -- local path or git repo
        files = { "src/parser.c", "src/scanner.cc" },
        branch = "main",
      },
      maintainers = { "@IndianBoy42" },
    }
  end
}
```

#### filetype

```lua
//- Load filetype.nvim

use {
  "nathom/filetype.nvim",
  config = function()
    require("filetype").setup {
      overrides = {
        extensions = {
          tf = "terraform",
          tfvars = "terraform",
          tfstate = "json",
        }
      }
    }
  end,
}
```

#### Telescope

[`telescope.nvim`](https://github.com/nvim-telescope/telescope.nvim) is a ridiculously fancy fuzzy-finder.

Not sure if I *must* specify `plenary.nvim` as a requirement when I'm already loading it. Better safe than sorry.

```lua
//- Load telescope.nvim
use { "nvim-telescope/telescope.nvim",
  requires = { {"nvim-lua/plenary.nvim"} },
}
```

##### Global key bindings for `telescope.nvim`

Showing the global `telescope.nvim` key bindings here, though Yarner will be
inserting them outside all this plugin definition stuff. I haven't figured out
how to do global keybindings in a plugin setup quite yet.

```lua
//- Add global bindings for telescope.nvim
map("n", "<leader>ff", "<cmd>lua require('telescope.builtin').find_files()<cr>")
map("n", "<leader>fg", "<cmd>lua require('telescope.builtin').live_grep()<cr>")
map("n", "<leader>fb", "<cmd>lua require('telescope.builtin').buffers()<cr>")
map("n", "<leader>fh", "<cmd>lua require('telescope.builtin').help_tags()<cr>")
```

#### null-ls

```lua
//- Load null-ls.nvim
use {
  "jose-elias-alvarez/null-ls.nvim",
  config = function()
    require("null-ls").setup({
      sources = {
        require("null-ls").builtins.formatting.stylua,
        require("null-ls").builtins.code_actions.proselint,
      }
    })
  end
}
```

#### which-key

I first bumped into the [`which-key`](https://github.com/folke/which-key.nvim) help menu in [Doom Emacs](https://github.com/hlissner/doom-emacs). Start a chained key binding like `SPC`, a menu pops up showing what chains are available. Indispensable there. Indispensable here. Thank goodness folks are porting so many Emacs packages to Neovim.

```lua
//- Load which-key.nvim
use {
  "folke/which-key.nvim",
  config = function()
    require("which-key").setup {}
  end
}
```

#### lualine

```lua
//- Load lualine.nvim
use { 'nvim-lualine/lualine.nvim',
  requires = { 'kyazdani42/nvim-web-devicons', opt = true },
  config = function()
    require('lualine').setup({
      -- options = { theme = "duskfox", }
    })
  end,
}
```

#### Programming Languages

A couple of the tools I use regularly require some special handling.

- [Black](https://github.com/psf/black) adds Python code formatting
- [nvim-nu](https://github.com/LhKipp/nvim-nu) adds support for [Nushell]({{< relref "/card/nushell.md" >}}) scripts
- [vim-asciidoctor](https://github.com/habamax/vim-asciidoctor) improves support for [Asciidoctor]({{< relref "/card/asciidoctor.md" >}}) — with block folding
- [vim-crystal](https://github.com/vim-crystal/vim-crystal) for [Crystal]({{< relref "/card/crystal.md" >}}) programming
- [Vim-Jinja2-Syntax](https://github.com/Glench/Vim-Jinja2-Syntax) highlights the Jinja / Nunjucks / Tera family of text template languages

```lua
//- Load programming language support
use "habamax/vim-asciidoctor"
use "vim-crystal/vim-crystal"
use "glench/vim-jinja2-syntax"
use {
  "LhKipp/nvim-nu",
  run = ":TSInstall nu",
  config = function()
    require("nu").setup{}
  end
}
use { "psf/black", cmd = {"Black"}}
```

#### Riv.vim

I bounce way too much between systems. Right now I use [Riv](https://github.com/gu-fan/riv.vim) when in Neovim. What can I say? I like reStructuredText.

`g:riv_file_link_style`
: use Riv's `:doc:` role instead of `[[...]]` for wiki links

```lua
//- Load riv.vim
use {
  "Rykka/riv.vim",
  config = function()
    riv_main = {
      path = "~/Dropbox/riv/main"
    }
    vim.g.riv_projects = {riv_main}
    vim.g.riv_file_link_style = 2
    vim.g.riv_highlight_code = "lua,python,cpp,javascript,sh,terraform|hcl"
  end
}
```

### Global options

```lua
opt.autoread = true
opt.background = 'dark'
opt.completeopt = {'menuone', 'noinsert', 'noselect'}  -- completion options (for deoplete)
opt.cursorline = true               -- highlight current line
opt.encoding = "utf-8"
opt.expandtab = true                -- spaces instead of tabs
opt.hidden = true                   -- enable background buffers
opt.ignorecase = true               -- ignore case in search
opt.joinspaces = false              -- no double spaces with join
opt.list = true                     -- show some invisible characters
opt.maxmempattern = 1000            -- for Riv
opt.mouse = "nv"                    -- Enable mouse in normal and visual modes
opt.number = true                   -- show line numbers
opt.relativenumber = true           -- number relative to current line
opt.scrolloff = 4                   -- lines of context
opt.shiftround = true               -- round indent
opt.shiftwidth = 2                  -- size of indent
opt.sidescrolloff = 8               -- columns of context
opt.smartcase = true                -- do not ignore case with capitals
opt.smartindent = true              -- insert indents automatically
opt.splitbelow = true              -- put new windows below current
opt.splitright = true               -- put new vertical splits to right
opt.termguicolors = true            -- truecolor support
opt.wildmode = {'list', 'longest'}  -- command-line completion mode
opt.wrap = false  -- disable line wrap

cmd[[filetype plugin on]]
cmd[[autocmd FileType * setlocal formatoptions-=cro]]
cmd[[autocmd FocusGained * checktime]]
cmd[[colorscheme nightfox]]

cmd[[autocmd BufWritePre *.py execute 'Black']]
cmd[[autocmd BufEnter *.astro set ft=astro]]
```

### Global variables

```lua
g.mapleader = ' '
g.maplocalleader = ','
g.python3_host_prog = '~/.pyenv/versions/neovim/bin/python'
g.markdown_fenced_languages = {
  "bash=sh",
  "python",
  "lua",
}
g.rst_syntax_code_list = { "python" }
```

### Diagnostics

Because I dislike unexpected floating text in my terminal.

```lua
vim.diagnostic.config({
  virtual_text = false,
})
```

### Keybindings

- `<bs>` clears search highlights

```lua
map("n", "<bs>", ":nohlsearch<cr>", { silent = true })

// ==> Add global bindings for telescope.nvim.
```

### Language Server Protocol (LSP)

For a fancy IDE-like experience when editing code.
And other structured text, if you're so inclined.

I pretty much use the standard suggested config.

```lua
local lsp_opts = { noremap=true, silent=true }
map('n', '<space>e', '<cmd>lua vim.diagnostic.open_float()<CR>', lsp_opts)
map('n', '[d', '<cmd>lua vim.diagnostic.goto_prev()<CR>', lsp_opts)
map('n', ']d', '<cmd>lua vim.diagnostic.goto_next()<CR>', lsp_opts)
map('n', '<space>q', '<cmd>lua vim.diagnostic.setloclist()<CR>', lsp_opts)

-- Use an on_attach function to only map the following keys
-- after the language server attaches to the current buffer
local lspconfig_on_attach = function(client, bufnr)
  -- Enable completion triggered by <c-x><c-o>
  vim.api.nvim_buf_set_option(bufnr, 'omnifunc', 'v:lua.vim.lsp.omnifunc')

  -- Mappings.
  -- See `:help vim.lsp.*` for documentation on any of the below functions
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gD', '<cmd>lua vim.lsp.buf.declaration()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gd', '<cmd>lua vim.lsp.buf.definition()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'K', '<cmd>lua vim.lsp.buf.hover()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gi', '<cmd>lua vim.lsp.buf.implementation()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<C-k>', '<cmd>lua vim.lsp.buf.signature_help()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>wa', '<cmd>lua vim.lsp.buf.add_workspace_folder()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>wr', '<cmd>lua vim.lsp.buf.remove_workspace_folder()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>wl', '<cmd>lua print(vim.inspect(vim.lsp.buf.list_workspace_folders()))<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>D', '<cmd>lua vim.lsp.buf.type_definition()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>rn', '<cmd>lua vim.lsp.buf.rename()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>ca', '<cmd>lua vim.lsp.buf.code_action()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', 'gr', '<cmd>lua vim.lsp.buf.references()<CR>', lsp_opts)
  vim.api.nvim_buf_set_keymap(bufnr, 'n', '<space>f', '<cmd>lua vim.lsp.buf.formatting()<CR>', lsp_opts)
end

require("lspconfig").pyright.setup { on_attach = lspconfig_on_attach, }

require("lspconfig").tsserver.setup {
  on_attach = lspconfig_on_attach,
}
```

And that's it!