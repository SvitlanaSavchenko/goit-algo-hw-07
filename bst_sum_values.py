class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def sum_tree_values(node):
    """Функція для обчислення суми всіх значень у двійковому дереві пошуку або AVL-дереві."""
    if node is None:
        return 0
    if not isinstance(node, TreeNode):
        raise ValueError("Неправильний тип вузла, очікується TreeNode.")
    if not isinstance(node.val, (int, float)):
        raise ValueError("Значення вузла має бути числом.")
    
    # Рекурсивно обчислюємо суму значень у лівому та правому піддеревах і додаємо значення поточного вузла
    return node.val + sum_tree_values(node.left) + sum_tree_values(node.right)

if __name__ == "__main__":
    try:
        # Приклад використання
        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(15)
        root.right.left = TreeNode(25)
        root.right.right = TreeNode(35)

        total_sum = sum_tree_values(root)
        print(f"Сума всіх значень у дереві: {total_sum}")
    except ValueError as e:
        print(f"Помилка: {e}")
