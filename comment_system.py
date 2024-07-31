class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає нову відповідь до коментаря."""
        if not isinstance(reply, Comment):
            raise TypeError("Відповідь має бути екземпляром класу Comment.")
        self.replies.append(reply)

    def remove_reply(self, reply=None):
        """Видаляє відповідь з коментаря. Змінює текст коментаря та встановлює прапорець is_deleted в True."""
        if reply is None:
            # Якщо не передано конкретну відповідь, видаляємо всі відповіді
            self.is_deleted = True
            self.text = "Цей коментар було видалено."
            self.replies = []
        else:
            # Видаляє конкретну відповідь
            if reply in self.replies:
                self.replies.remove(reply)
                reply.text = "Цей коментар було видалено."
                reply.is_deleted = True
            else:
                raise ValueError("Відповідь не знайдена серед відповідей коментаря.")

    def display(self, level=0):
        """Рекурсивно виводить коментар та всі його відповіді з відступами для ієрархії."""
        indent = "  " * level
        if self.is_deleted:
            print(f"{indent}Цей коментар було видалено.")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

if __name__ == "__main__":
    # Приклад використання
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()
