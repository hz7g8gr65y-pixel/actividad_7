from repositories.user_repository import InventoryRepository
from services.user_service import InventoryService
from ui.app_window import AppWindow

def main():
    repository = InventoryRepository()
    service = InventoryService(repository)

    app_window = AppWindow(service)
    app_window.mainloop()

if __name__ == "__main__":
    main()
