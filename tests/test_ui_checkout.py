import re
from playwright.sync_api import Page, expect


def test_order_checkout_flow_and_totals(page: Page):
    # Step 1: Log in to the platform
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url(re.compile(".*inventory.html"))

    # Step 2: Add item to cart and open cart
    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    expect(page.locator(".cart_item")).to_have_count(1)

    # Step 3: Fill out customer info
    page.click("#checkout")
    page.fill("#first-name", "Jane")
    page.fill("#last-name", "Doe")
    page.fill("#postal-code", "10001")
    page.click("#continue")

    # Step 4: Extract pricing figures from UI
    item_total_text = page.locator(".summary_subtotal_label").inner_text()
    tax_text = page.locator(".summary_tax_label").inner_text()
    total_text = page.locator(".summary_total_label").inner_text()

    item_total = float(item_total_text.replace("Item total: $", ""))
    tax = float(tax_text.replace("Tax: $", ""))
    total = float(total_text.replace("Total: $", ""))

    # Step 5: Core Business Rule Assertion
    assert round(item_total + tax, 2) == round(total, 2), (
        f"Pricing Mismatch! {item_total} + {tax} != {total}"
    )

    # Step 6: Finalize order and confirm success
    page.click("#finish")
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")