class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def find_min_value(node):
    """Функція для знаходження найменшого значення в двійковому дереві пошуку або AVL-дереві."""
    if node is None:
        raise ValueError("Дерево порожнє, неможливо знайти мінімальне значення.")
    
    current = node
    # Продовжуємо рухатись вліво, поки не знайдемо крайній лівий вузол
    while current.left is not None:
        current = current.left
    return current.val

if __name__ == "__main__":
    try:
        # Приклад використання
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)

        min_value = find_min_value(root)
        print(f"Мінімальне значення в дереві: {min_value}")
    except ValueError as e:
        print(e)
