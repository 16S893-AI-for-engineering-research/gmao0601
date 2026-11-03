// Recreate the approved workflow figure: swift img/generate_new_workflow.swift
// Visual summary of the reviewed plan; Backlog tasks remain authoritative.
import AppKit

let width = 1800, height = 2690
let output = URL(fileURLWithPath: #filePath).deletingLastPathComponent().appendingPathComponent("new_workflow.png")
let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height,
    bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false,
    colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: bitmap)
let ctx = NSGraphicsContext.current!.cgContext
ctx.translateBy(x: 0, y: CGFloat(height))
ctx.scaleBy(x: 1, y: -1)

func color(_ hex: String) -> NSColor {
    let n = UInt32(hex, radix: 16)!
    return NSColor(red: CGFloat((n >> 16) & 255)/255, green: CGFloat((n >> 8) & 255)/255,
                   blue: CGFloat(n & 255)/255, alpha: 1)
}
let ink = "183D50", muted = "526E7C", line = "809EAC", blue = "1683B4"
func rect(_ x: CGFloat, _ y: CGFloat, _ w: CGFloat, _ h: CGFloat, _ fill: String,
          radius: CGFloat = 18, stroke: String? = nil, thickness: CGFloat = 2) {
    let p = CGPath(roundedRect: CGRect(x:x, y:y, width:w, height:h), cornerWidth:radius, cornerHeight:radius, transform:nil)
    ctx.addPath(p); ctx.setFillColor(color(fill).cgColor); ctx.fillPath()
    if let stroke = stroke {
        ctx.addPath(p); ctx.setStrokeColor(color(stroke).cgColor); ctx.setLineWidth(thickness); ctx.strokePath()
    }
}
func text(_ value: String, _ x: CGFloat, _ y: CGFloat, _ size: CGFloat = 22,
          _ shade: String = "183D50", bold: Bool = false, serif: Bool = false) {
    // NSString drawing receives a local upright coordinate system.
    let name = serif ? (bold ? "Georgia-Bold" : "Georgia") : (bold ? "Helvetica-Bold" : "Helvetica")
    let font = NSFont(name:name, size:size) ?? NSFont.systemFont(ofSize:size)
    let attrs: [NSAttributedString.Key:Any] = [.font:font, .foregroundColor:color(shade)]
    let s = value as NSString
    let extent = s.size(withAttributes:attrs)
    ctx.saveGState(); ctx.translateBy(x:x, y:y+extent.height); ctx.scaleBy(x:1,y:-1)
    s.draw(at:.zero, withAttributes:attrs); ctx.restoreGState()
}
func path(_ pts: [(CGFloat,CGFloat)], dashed: Bool = false, arrow: Bool = true, shade: String = "809EAC") {
    guard pts.count > 1 else { return }
    ctx.saveGState(); ctx.setStrokeColor(color(shade).cgColor); ctx.setLineWidth(3)
    ctx.setLineJoin(.round); ctx.setLineCap(.round)
    if dashed { ctx.setLineDash(phase:0, lengths:[9,8]) }
    ctx.beginPath(); ctx.move(to:CGPoint(x:pts[0].0,y:pts[0].1))
    for p in pts.dropFirst() { ctx.addLine(to:CGPoint(x:p.0,y:p.1)) }
    ctx.strokePath(); ctx.restoreGState()
    if arrow {
        let a = pts[pts.count-2], b = pts.last!
        let theta = atan2(b.1-a.1,b.0-a.0), len: CGFloat = 12, spread: CGFloat = 0.43
        ctx.setFillColor(color(shade).cgColor); ctx.beginPath(); ctx.move(to:CGPoint(x:b.0,y:b.1))
        ctx.addLine(to:CGPoint(x:b.0-len*cos(theta-spread),y:b.1-len*sin(theta-spread)))
        ctx.addLine(to:CGPoint(x:b.0-len*cos(theta+spread),y:b.1-len*sin(theta+spread)))
        ctx.closePath(); ctx.fillPath()
    }
}
func band(_ y: CGFloat, _ h: CGFloat, _ label: String, _ fill: String) {
    rect(35,y,1730,h,fill,radius:24)
    text(label,62,y+18,18,"146185",bold:true)
}
let cardW: CGFloat = 440, cardH: CGFloat = 135
func card(_ id: String, _ x: CGFloat, _ y: CGFloat, _ lines: [String], _ note: String,
          state: String = "TO DO") {
    let edge = state == "READY NOW" ? blue : state == "DRAFT" ? "A18BB5" : "8DA7B6"
    let fill = state == "READY NOW" ? "DCF0FF" : state == "DRAFT" ? "F7F0FC" : "FFFFFF"
    rect(x+2,y+6,cardW,cardH,"D7E2E6",radius:16)
    rect(x,y,cardW,cardH,fill,radius:16,stroke:edge,thickness:2.5)
    text(id,x+20,y+13,18,ink,bold:true)
    let pillW: CGFloat = state == "READY NOW" ? 136 : 108
    rect(x+cardW-pillW-16,y+12,pillW,27,edge,radius:14)
    text(state,x+cardW-pillW-4,y+16,15,"FFFFFF",bold:true)
    for (i,l) in lines.enumerated() { text(l,x+20,y+49+CGFloat(i)*27,23,ink,serif:true) }
    text(note,x+20,y+108,16,muted)
}

rect(0,0,CGFloat(width),CGFloat(height),"F4F9FC",radius:0)
rect(0,0,CGFloat(width),185,"D9F0FD",radius:0)
text("US3D Plugin Workflow",60,28,46,ink,bold:true,serif:true)
text("Approved plan  •  Reusable capabilities → safe initialization → validation → research",62,91,22,muted)
rect(1170,35,14,14,blue,radius:7); text("Ready now",1195,29,18)
rect(1335,35,14,14,"8DA7B6",radius:7); text("To do",1360,29,18)
rect(1460,35,14,14,"A18BB5",radius:7); text("Deferred",1485,29,18)
path([(1175,80),(1230,80)],arrow:false); text("Required progression",1245,69,17)
path([(1175,117),(1230,117)],dashed:true,arrow:false,shade:"B28C4B")
text("Approval / review gate",1245,106,17)
text("Agent: prepare + analyze     |     You: compile + run US3D + return evidence",62,140,20,ink,bold:true)

band(210,210,"01  FOUNDATIONS", "E8F5FC")
band(445,400,"02  REUSABLE CAPABILITIES", "EDF7F2")
band(885,345,"03  SAFE INITIALIZATION", "F2EFFA")
band(1270,270,"04  EQUATIONS + EXECUTION CHECK", "FFF8E7")
band(1575,745,"05  HARTMANN-FLOW VALIDATION  •  ONE SHARED BENCHMARK, THREE CASES", "EFF5FA")
band(2355,240,"06  RESEARCH  •  DEFERRED UNTIL VALIDATION PASSES", "F9F0F5")

// Main progression; redundant transitive dependencies are deliberately omitted.
path([(900,400),(900,435),(330,435),(330,515)])
path([(900,400),(900,515)])
path([(900,400),(900,435),(1470,435),(1470,515)])
path([(330,650),(330,695)])
path([(330,830),(330,855),(500,855),(500,945)])
path([(900,650),(900,675),(620,675),(620,862),(520,862),(520,945)])
path([(1470,650),(1470,872),(540,872),(540,945)])
path([(550,1012),(680,1012)])
path([(1120,1012),(1250,1012)])
path([(1470,1080),(1470,1100),(1740,1100),(1740,1248),(620,1248),(620,1340)])
path([(840,1407),(1000,1407)])
path([(1220,1475),(1220,1557),(900,1557),(900,1640)])
path([(900,1775),(900,1830)],dashed:true,shade:"B28C4B")
path([(900,1965),(900,1995),(520,1995),(520,2030)])
path([(900,1965),(900,1995),(1280,1995),(1280,2030)])
path([(520,2165),(520,2200),(800,2200),(800,2230)])
path([(1280,2165),(1280,2200),(1000,2200),(1000,2230)])
path([(900,2290),(900,2420)],dashed:true,shade:"B28C4B")

card("TASK-1",680,265,["Inventory manuals + examples","Record missing files and questions"],"References: .pi/ref-library/",state:"READY NOW")
text("Sources, not assumptions",90,290,25,ink,bold:true,serif:true)
text("Use original manual citations.",90,330,21,muted)
text("Preserve supplied examples.",90,360,21,muted)
text("Current starting point",1250,290,25,ink,bold:true,serif:true)
text("All work is unstarted.",1250,330,21,muted)
text("No target-environment agent access.",1250,360,21,muted)

card("TASK-2",110,515,["Equations → approved hooks","Readable + structured mapping"],"Citations, stable IDs, unresolved questions")
card("TASK-4",680,515,["Template → new US3D input","Explicit settings + change report"],"Do not modify the original input.inp")
card("TASK-5",1250,515,["Settings → Slurm script","Choose pre / solve / post stages"],"Generate only; never auto-submit")
card("TASK-3",110,695,["Hooks → plugin skeleton","Initialize approved variables only"],"Documented behavior-preserving handling")
text("Approval before generation",700,705,26,ink,bold:true,serif:true)
text("Approve skill/tool packaging; approve mappings before generation.",700,747,22,muted)
text("Never guess missing settings or assume zero means “no change.”",700,781,22,muted)

card("TASK-6",110,945,["Test initialized hooks","Existing CFD outputs unchanged"],"USER RUN + AGENT COMPARISON")
card("TASK-7",680,945,["Initialize custom diffusion","Keep equation contributions inactive"],"New state only; existing solver values preserved")
card("TASK-8",1250,945,["Test diffusion initialization","Existing CFD outputs unchanged"],"USER RUN + AGENT COMPARISON")
rect(85,1122,1630,78,"E7E1F2",radius:14)
text("No-plugin baseline vs. initialization-only plugin: initialization + a few matching steps",110,1134,23,ink,bold:true)
text("Compare all existing CFD values exactly by default. Check new variables separately. Missing evidence cannot pass.",110,1167,21,muted)

card("TASK-9",400,1340,["Implement supplied equations","Independent mathematical checks"],"Split bounded contributions only when needed")
card("TASK-10",1000,1340,["Verify the active plugin runs","Compile, load, initialize + short run"],"PASS = ready for validation, not validated")

card("TASK-11 · PARENT",680,1640,["Coordinate shared validation","Approve reference + case criteria"],"Parent remains open for final synthesis")
text("Before running",95,1665,25,ink,bold:true,serif:true)
text("Confirm model assumptions,",95,1705,22,muted)
text("electrical conditions and metrics.",95,1737,22,muted)
text("Three Hartmann numbers",1250,1665,25,ink,bold:true,serif:true)
text("Select actual values with you.",1250,1705,22,muted)
text("No post-hoc threshold relaxation.",1250,1737,22,muted)
card("TASK-11.1",680,1830,["Weak-field Hartmann case","Establish reusable case workflow"],"USER RUN + quantitative comparison")
text("Complete this case first",1170,1855,23,ink,bold:true)
text("Reuse reference + comparator below.",1170,1890,21,muted)
card("TASK-11.2",300,2030,["Moderate-field Hartmann case","Convergence + mesh checks"],"USER RUN + quantitative comparison")
card("TASK-11.3",1060,2030,["Stronger-field Hartmann case","Resolve thinner Hartmann layers"],"USER RUN + quantitative comparison")
rect(420,2230,960,60,"E0EBF2",radius:15,stroke:"91AAB8")
text("TASK-11 REVIEW: all three cases pass + limitations recorded",455,2247,23,ink,bold:true)

card("DRAFT-1",680,2420,["Research cases — scope later","Define questions, cases + budget"],"Not an executable agent assignment yet",state:"DRAFT")
text("Do not invent research scope",95,2445,24,ink,bold:true,serif:true)
text("Refine after validation is complete.",95,2485,21,muted)
text("User approval required",1250,2445,24,ink,bold:true,serif:true)
text("Prepare → user runs → agent analyzes.",1250,2485,21,muted)

text("Reviewed-plan snapshot • Backlog tasks are authoritative • Transitive links omitted for readability",62,2620,19,muted)
text("Reference: backlog/docs/doc-1 — agreed plan and decision log",62,2650,18,muted)

NSGraphicsContext.restoreGraphicsState()
try bitmap.representation(using:.png,properties:[:])!.write(to:output)
print("Saved \(output.path) (\(width) × \(height))")
