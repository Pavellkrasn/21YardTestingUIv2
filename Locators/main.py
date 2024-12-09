class Main:

    BUTTON_REGISTRATION_HEADLESS = "a[href='/registration'][type='button'][class*='md:!hidden']"
    BUTTON_LOGIN_HEADLESS = "a[href='/login/'][type='button'][class*='md:!hidden']"
    BUTTON_HEADLESS_MENU = "button[aria-haspopup='menu']"


    MENU_ITEM_APPLICATIONS = "a[role='menuitem'][href='/applications']"
    MENU_ITEM_MY_APPLICATIONS = "a[role='menuitem'][href='/myApplications/active']"
    MENU_ITEM_TARIFFS = "a[role='menuitem'][href='/tariffs/responseApplication']"
    MENU_ITEM_TEMPLATES = "a[role='menuitem'][href='/documents/templates']"
    MENU_ITEM_HELP = "a[role='menuitem'][href='https://t.me/manager21yard']"

    WRAPPER_HEADLESS_MENU ="#headlessui-portal-root"


    TITLE_MAIN = "//h1[contains(@class,'sm:text-center')]"
    TITLE_PARTNER_SECTOR = "//h2[contains(@class,'md:mb-4')]"

    LIST_OF_COMPANIES_PARTNERS_LOGO = "//body/div/div/section/section/div/div[3]/div[1]/div"
    LIST_OF_COMPANIES_PARTNERS_DOCUMENT = "//div//div//div//div//div[2]//div[1]//img"
    LIST_OF_REGISTRATION_AND_APPLICATION_BUTTONS_ON_MAIN_PAGE = ("//a[contains(.//text(), 'Начать сейчас') "
                                                                  "or contains(.//text(), 'Попробовать сейчас')]")

    LIST_OF_REGISTRATION_BUTTONS_ON_MAIN_PAGE = "a[href='/registration'][type='button']:not(.md\:\!hidden)"
    LIST_OF_APPLICATIONS_BUTTONS_ON_MAIN_PAGE = "a[href='/applications'][type='button']"