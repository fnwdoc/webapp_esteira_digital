from playwright.sync_api import sync_playwright, Page, expect
import os

def run_verification(page: Page):
    """
    Verifies that a product can be created successfully.
    """
    # 1. Arrange: Go to the index.html page.
    # Use os.path.abspath to get the full path to the file.
    file_path = os.path.abspath('index.html')
    page.goto(f'file://{file_path}')

    # 2. Act: Create a new product.
    # Click the 'Cadastrar Produto' button to open the modal.
    page.get_by_role("button", name="Cadastrar Produto").click()

    # Fill in the product details.
    page.locator("#productTitle").fill("Test Product")
    page.locator("#productPrice").fill("100")
    page.locator("#productDescription").fill("This is a test product.")

    # Click the 'Salvar Produto' button.
    page.locator("#btn-save").click()

    # 3. Assert: Confirm the product was created.
    # Look for the new product card in the 'LTi' column.
    product_list = page.locator("#lti-list")
    new_product_card = product_list.locator(".product-card", has_text="Test Product")

    # Use expect to wait for the element to be visible.
    expect(new_product_card).to_be_visible()
    expect(new_product_card.locator("h6")).to_have_text("Test Product")
    expect(new_product_card.locator(".price")).to_have_text("R$ 100,00")


    # 4. Screenshot: Capture the final result for visual verification.
    page.screenshot(path="jules-scratch/verification/verification.png")

# Boilerplate to run the verification function.
def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run_verification(page)
        browser.close()

if __name__ == "__main__":
    main()
