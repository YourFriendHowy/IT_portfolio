```
-- ~/.config/nvim/lua/plugins/toggleterm.lua
return {
  "akinsho/toggleterm.nvim",
  version = "*",

  config = function()
    local Terminal = require("toggleterm.terminal").Terminal

    local bottom_term = Terminal:new({
      id = 1,
      direction = "horizontal",
    })

    -- <leader>t → toggle terminal
    vim.keymap.set({ "n", "t" }, "<leader>t", function()
      bottom_term:toggle()
    end)

    -- <leader>rp → run python (atomic action)
    vim.keymap.set({ "n", "t" }, "<leader>rp", function()
      vim.cmd("write")
      
      -- figure out which file to run
      local file
      if vim.bo.filetype == "toggleterm" then
        file = vim.fn.expand("#:p")  -- previous buffer
      else
        file = vim.fn.expand("%:p")
      end

      bottom_term:open()
      bottom_term:send("python " .. vim.fn.fnameescape(file) .. "\r")
      vim.cmd("startinsert")
    end)
  end,
}


```