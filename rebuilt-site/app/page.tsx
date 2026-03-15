import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export default function Home() {
  return (
    <div className="container mx-auto py-12 px-6">
      <section className="text-center mb-16">
        <h1 className="text-4xl font-bold font-heading mb-4">Viatrexx Bioregulation Formulas</h1>
        <p className="text-xl text-muted-foreground mb-8">Advanced integrative solutions for detox, drainage, and regeneration.</p>
        <div className="flex justify-center gap-4">
          <Button size="lg">Explore Products</Button>
          <Button variant="outline" size="lg">Our Science</Button>
        </div>
      </section>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        <Card>
          <CardHeader>
            <CardTitle>Detox & Drainage</CardTitle>
            <CardDescription>Support your body's natural elimination pathways.</CardDescription>
          </CardHeader>
          <CardContent>
            <img src="/public/assets/optimized/clinical-research.webp" alt="Research" className="rounded-md mb-4" />
            <Button variant="link" className="px-0">Learn more</Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Immune Support</CardTitle>
            <CardDescription>Advanced peptides and bioregulators for a resilient system.</CardDescription>
          </CardHeader>
          <CardContent>
             <img src="/public/assets/optimized/ez-heartbeat-science.webp" alt="Science" className="rounded-md mb-4" />
            <Button variant="link" className="px-0">Learn more</Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Metabolic Health</CardTitle>
            <CardDescription>Targeted support for cellular energy and metabolism.</CardDescription>
          </CardHeader>
          <CardContent>
            <img src="/public/assets/optimized/hexagon-bg.webp" alt="Metabolic" className="rounded-md mb-4" />
            <Button variant="link" className="px-0">Learn more</Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
