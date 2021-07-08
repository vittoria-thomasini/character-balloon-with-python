## 1-Create a function that says a given message inside a text "balloon"

 def say_in_ballon(self, message):
        messages = message.split('\n')
        longest_line_size = (max([len(m) for m in messages]))
        print('-' * longest_line_size)

        if len(messages)==1:
            print(f'< {messages} >')
        else:
            print(f'/ {messages[0].center(longest_line_size)} \\')    
            for str_idx in range(len(messages) - 2):
                print(f'| {messages[str_idx+1].center(longest_line_size)} |')
    
            print(f'\\ {messages[-1].center(longest_line_size)} /')
      
say_in_ballon('Hello there, General Kenobi')
say_in_ballon('Hello there,\nGeneral Kenobi')
say_in_ballon('Hello\nthere,\nGeneral Kenobi')
say_in_ballon('Hello\nthere,\nGeneral\nKenobi')
