class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def find_max_value(node):
    """Функція для знаходження найбільшого значення в двійковому дереві пошуку або AVL-дереві."""
    if node is None:
        raise ValueError("Дерево порожнє, неможливо знайти максимальне значення.")
    
    current = node
    # Продовжуємо рухатись вправо, поки не знайдемо крайній правий вузол
    while current.right is not None:
        current = current.right
    return current.val

if __name__ == "__main__":
    try:
        # Приклад використання
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.right.right = TreeNode(40)

        max_value = find_max_value(root)
        print(f"Максимальне значення в дереві: {max_value}")
    except ValueError as e:
        print(e)
