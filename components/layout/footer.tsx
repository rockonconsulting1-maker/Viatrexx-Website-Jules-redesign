import * as React from "react"
import Link from "next/link"
import { Facebook, Instagram, Linkedin, Twitter } from "lucide-react"

const Footer = () => {
  const currentYear = new Date().getFullYear()

  const quickLinks = [
    { name: "Home", href: "/" },
    { name: "Products", href: "/products" },
    { name: "Educational Resources", href: "/resources" },
  ]

  const companyLinks = [
    { name: "About Us", href: "/about" },
    { name: "Our Science", href: "/science" },
    { name: "Contact", href: "/contact" },
  ]

  const legalLinks = [
    { name: "Medical Disclaimer", href: "/medical-disclaimer" },
    { name: "Refund & Return Policy", href: "/refund-policy" },
    { name: "Shipping Policy", href: "/shipping-policy" },
    { name: "Copyright Policy", href: "/copyright-policy" },
  ]

  return (
    <footer className="bg-background border-t">
      <div className="container px-6 py-12 mx-auto">
        <div className="grid grid-cols-1 gap-12 lg:grid-cols-4">
          <div className="flex flex-col gap-4">
            <Link href="/" className="flex items-center">
              <img
                src="/storage.googleapis.com/msgsndr/Wv6kWdgCt9mf9ZTVwPw4/media/68055cff29d62943f33635ea.webp"
                alt="Viatrexx Logo"
                className="h-10 w-auto"
              />
            </Link>
            <p className="max-w-sm text-muted-foreground text-sm">
              Viatrexx is a wellness company dedicated to developing integrative formulas that address drainage, detox, repair, regeneration, and immune support.
            </p>
            <div className="flex gap-4">
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Facebook className="h-5 w-5" />
                <span className="sr-only">Facebook</span>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Twitter className="h-5 w-5" />
                <span className="sr-only">Twitter</span>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Linkedin className="h-5 w-5" />
                <span className="sr-only">LinkedIn</span>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <Instagram className="h-5 w-5" />
                <span className="sr-only">Instagram</span>
              </a>
            </div>
          </div>

          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">Quick Links</h3>
            <ul className="flex flex-col gap-2">
              {quickLinks.map((link) => (
                <li key={link.name}>
                  <Link href={link.href} className="text-sm text-muted-foreground hover:text-primary transition-colors">
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">Company</h3>
            <ul className="flex flex-col gap-2">
              {companyLinks.map((link) => (
                <li key={link.name}>
                  <Link href={link.href} className="text-sm text-muted-foreground hover:text-primary transition-colors">
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div className="flex flex-col gap-4">
            <h3 className="text-sm font-semibold uppercase tracking-wider">Join Our Newsletter</h3>
            <p className="text-sm text-muted-foreground">Get the latest updates on wellness and our science.</p>
            {/* Newsletter placeholder */}
            <div className="flex gap-2">
              <input
                type="email"
                placeholder="Email address"
                className="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
              />
              <button className="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 bg-primary text-primary-foreground hover:bg-primary/90 px-4 py-2">
                Join
              </button>
            </div>
          </div>
        </div>

        <div className="mt-12 pt-8 border-t flex flex-col md:flex-row items-center justify-between gap-4">
          <div className="flex flex-wrap items-center justify-center gap-4">
            {legalLinks.map((link, index) => (
              <React.Fragment key={link.name}>
                <Link href={link.href} className="text-xs text-muted-foreground hover:text-primary transition-colors">
                  {link.name}
                </Link>
                {index < legalLinks.length - 1 && <span className="text-muted-foreground/30">|</span>}
              </React.Fragment>
            ))}
          </div>
          <p className="text-xs text-muted-foreground">
            &copy; {currentYear} Viatrexx. All Rights Reserved.
          </p>
        </div>
      </div>
    </footer>
  )
}

export { Footer }
