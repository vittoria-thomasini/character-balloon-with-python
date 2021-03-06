## 1-Create a function that says a given message inside a text "balloon"
## 2-Create a class named PythonSays which has a __init__ and a say(message) method
## 2.1-Move the say_in_balloon to the say method
class PythonSays():
    def __init__(self):
        pass
        
    def say(self, message):
        messages = message.split('\n')
        longest_line_size = (max([len(m) for m in messages]))
        line = '  ' + '-' * longest_line_size
        print(line)
        if len(messages)==1:
            print(f'< {messages} >')
        else:
            print(f'/ {messages[0].center(longest_line_size)} \\')    
            for str_idx in range(len(messages) - 2):
                print(f'| {messages[str_idx+1].center(longest_line_size)} |')
            
            print(f'\\ {messages[-1].center(longest_line_size)} /')
        print(line)
        print(general_grievous)
        
general_grievous = '''
                       \\\\ 
                         \\\                                      
                            \\    ...... .....                                  
                                .... ..........*.                               
                              *  .% *.  .......         .                       
                        .    / ...@...........  @   /   ..                      
                     ....   ** ...& ..........  &   */  ..                      
                  ....      // ...@........ ..  &    *  ......                  
                ......   /*(/. ...@...........  @     #*.  ....                 
                ....* #%  **. . ..@........... .&      ** &(....                
                ..../ %&% *       @    ...      #        *&& .. .               
                ..    %@#* %&@@@@@@#/ ...      #@@@@@@&(*%@(  ....              
                    * #&(*/#&@@@/(%&@% ..    /@@%@%@@@&/ #%( ....               
                 ... *(%%& (@@%%@@@/   .       *#@@%&@@**&(  ...                
                  . .  #@@/  */*              ****/#/*  #@#.....                
                   * ..  #@#**////**        * ****///////   ..                  
                     .   */((@%((/**         **///(/##(/*   .                   
                      /   **/@@@@%/***        /*/#@@@*/*   .                    
                       %*   **@@@@(*         **/#@@@%    .                      
                         /    @@%@(*         **/(#@&@   .                       
                       /%#@.. *@@@&*    **** **/@@@@   .&                       
                     #%%#@@@ ..*@&#**((*#/#%%#*/(&@* . @##&                     
    *              /#&&(&@@@@ .%@@@*/(/////%#%/*@@@@. @@@@#@(                   
                 */((&#@@@@@@@..&@**/%((@//%##(//@@&.@@@@@%#&(*                 
               *//(%&#&&@@@@@@@ @@* /%%/@//##%(*/@@./@@@@@%%&#(/*               
              /(/#%&@@@@&@@@@@@&//* /&((/(((%&(*/@@@@@@@@&%@@@&#**              
             *//#%&@@@@((@@@@@&@@(* //(&%%%%##(*/@@@@@@@&%@@@@@&%*              
         %@@*((##&@@@@@@@@@@@@@@@&**#@@@@@@@@@#**@@@@@@&&@@@@@@@&#/* %%         
          @@*#%%&@@@@&@@@@%%@@&@@@**/@@@@@@@@@/*@@@@@@@@@@@@@@@@@%((            
           ***@&@@&@@@@@&@@@@@&@@@@/(@@@@@@&@%/#@@@@@@@@@@@@@@@@@&&  *          
           */*//@%&%@(@@&@@@@@@@@@/#/@&&@@@@@%&&@@@@@@@@@@@@@@@@@@  **          
          //******%&@@@@@&@@@@@@@@@@/* **  ***/@@@@@@@@@@@@@@&@&    */*         
          (/*** ***/&@@@@@@@@@@@@/**  *(   ** **/@@@@@@@@@@@@&  *   *((         

'''
character = PythonSays()
character.say('Hello there, General Kenobi')
character.say('Hello there,\nGeneral Kenobi')
character.say('Hello\nthere,\nGeneral Kenobi')
character.say('Hello\nthere,\nGeneral\nKenobi')
