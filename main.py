from flet import *
import ollama as ai



def main(page:Page):
    page.padding = padding.only(top=55)
    page.scroll = True

    def _function(e:ControlEvent):
        if not user_input.value:
            page.add(Text("Error message box cannot be empty"))
            page.update()
        if user_input.value:
            response = ai.chat(model='llama3', messages=[{"role": 'user', "content": user_input.value}])
            user_input.value = ""
            txt = Text(value=response['message']['content'])
            page.add(txt)
            print(response['message']['content'])
            page.update()


    user_input:TextField = TextField(hint_text="enter message", width=350, autocorrect=True)
    _controls_row:Row = Row(
        controls=[user_input, IconButton(icon=icons.SEND, on_click=_function)],
        alignment='center',
        spacing=5
    )
    answer = Column()

    _container:Container = Container()

    page.add(
        _controls_row
    )

app(target=main)