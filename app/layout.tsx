import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Pahal Foundation NGO',
  description: 'Pahal Foundation - Building a better future through education and community service',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
