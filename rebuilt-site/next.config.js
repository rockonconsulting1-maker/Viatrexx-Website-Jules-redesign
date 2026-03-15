/** @type {import('next').NextConfig} */
const nextConfig = {
  async redirects() {
    return [
      {
        source: '/index.html',
        destination: '/',
        permanent: true,
      },
      {
        source: '/home.html',
        destination: '/',
        permanent: true,
      },
      {
        source: '/about.html',
        destination: '/about',
        permanent: true,
      },
      {
        source: '/products.html',
        destination: '/products',
        permanent: true,
      },
      {
        source: '/products/collections/index.html',
        destination: '/collections',
        permanent: true,
      },
      {
        source: '/product-details/product/:name.html',
        destination: '/products/:name',
        permanent: true,
      },
      {
        source: '/products/collections/:name.html',
        destination: '/collections/:name',
        permanent: true,
      }
    ]
  },
}

module.exports = nextConfig
