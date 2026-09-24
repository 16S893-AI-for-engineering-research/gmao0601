import AppKit

let width = 1600
let height = 900
let output = "img/magnetic-window-diagram.png"

let rep = NSBitmapImageRep(
    bitmapDataPlanes: nil,
    pixelsWide: width,
    pixelsHigh: height,
    bitsPerSample: 8,
    samplesPerPixel: 4,
    hasAlpha: true,
    isPlanar: false,
    colorSpaceName: .deviceRGB,
    bytesPerRow: 0,
    bitsPerPixel: 0
)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)

func color(_ hex: UInt32, alpha: CGFloat = 1) -> NSColor {
    NSColor(
        red: CGFloat((hex >> 16) & 0xff) / 255,
        green: CGFloat((hex >> 8) & 0xff) / 255,
        blue: CGFloat(hex & 0xff) / 255,
        alpha: alpha
    )
}

func roundedRect(_ rect: NSRect, radius: CGFloat, fill: NSColor, stroke: NSColor? = nil, lineWidth: CGFloat = 1) {
    let path = NSBezierPath(roundedRect: rect, xRadius: radius, yRadius: radius)
    fill.setFill()
    path.fill()
    if let stroke {
        stroke.setStroke()
        path.lineWidth = lineWidth
        path.stroke()
    }
}

func text(_ value: String, x: CGFloat, y: CGFloat, size: CGFloat, weight: NSFont.Weight = .regular, fill: NSColor, width: CGFloat = 700, alignment: NSTextAlignment = .left) {
    let paragraph = NSMutableParagraphStyle()
    paragraph.alignment = alignment
    paragraph.lineBreakMode = .byWordWrapping
    let attrs: [NSAttributedString.Key: Any] = [
        .font: NSFont.systemFont(ofSize: size, weight: weight),
        .foregroundColor: fill,
        .paragraphStyle: paragraph
    ]
    (value as NSString).draw(in: NSRect(x: x, y: y, width: width, height: size * 2.7), withAttributes: attrs)
}

func line(from a: NSPoint, to b: NSPoint, stroke: NSColor, width: CGFloat = 3, dash: [CGFloat] = []) {
    let p = NSBezierPath()
    p.move(to: a)
    p.line(to: b)
    p.lineWidth = width
    if !dash.isEmpty { p.setLineDash(dash, count: dash.count, phase: 0) }
    p.lineCapStyle = .round
    stroke.setStroke()
    p.stroke()
}

func arrow(from a: NSPoint, to b: NSPoint, stroke: NSColor, width: CGFloat = 4) {
    line(from: a, to: b, stroke: stroke, width: width)
    let angle = atan2(b.y - a.y, b.x - a.x)
    let length: CGFloat = 16
    let spread: CGFloat = 0.52
    let p = NSBezierPath()
    p.move(to: b)
    p.line(to: NSPoint(x: b.x - length * cos(angle - spread), y: b.y - length * sin(angle - spread)))
    p.move(to: b)
    p.line(to: NSPoint(x: b.x - length * cos(angle + spread), y: b.y - length * sin(angle + spread)))
    p.lineWidth = width
    p.lineCapStyle = .round
    stroke.setStroke()
    p.stroke()
}

let navy = color(0x123247)
let blue = color(0x1F6B8C)
let cyan = color(0x48B9D8)
let orange = color(0xF27635)
let warmWhite = color(0xF7FAFC)
let gray = color(0xCBD3D9)
let darkGray = color(0x52616B)
let paleBlue = color(0xE9F5F9)

// Background and framed illustration area.
warmWhite.setFill()
NSRect(x: 0, y: 0, width: width, height: height).fill()
roundedRect(NSRect(x: 48, y: 48, width: 1504, height: 804), radius: 28, fill: .white, stroke: color(0xD9E4EA), lineWidth: 2)
text("MAGNETIC WINDOW CONCEPT", x: 100, y: 770, size: 25, weight: .semibold, fill: blue, width: 800)
text("Temporarily opening a path through the plasma sheath", x: 100, y: 665, size: 42, weight: .bold, fill: navy, width: 1160)

// Pale atmosphere panel.
roundedRect(NSRect(x: 100, y: 145, width: 1400, height: 520), radius: 22, fill: paleBlue)

// Outer shock layer.
let shock = NSBezierPath()
shock.move(to: NSPoint(x: 1480, y: 555))
shock.line(to: NSPoint(x: 700, y: 555))
shock.curve(to: NSPoint(x: 300, y: 365), controlPoint1: NSPoint(x: 490, y: 555), controlPoint2: NSPoint(x: 300, y: 500))
shock.curve(to: NSPoint(x: 700, y: 185), controlPoint1: NSPoint(x: 300, y: 235), controlPoint2: NSPoint(x: 490, y: 185))
shock.line(to: NSPoint(x: 1480, y: 185))
shock.line(to: NSPoint(x: 1480, y: 555))
blue.setFill()
shock.fill()

// Plasma sheath.
let plasma = NSBezierPath()
plasma.move(to: NSPoint(x: 1480, y: 510))
plasma.line(to: NSPoint(x: 690, y: 510))
plasma.curve(to: NSPoint(x: 355, y: 365), controlPoint1: NSPoint(x: 515, y: 510), controlPoint2: NSPoint(x: 355, y: 462))
plasma.curve(to: NSPoint(x: 690, y: 230), controlPoint1: NSPoint(x: 355, y: 270), controlPoint2: NSPoint(x: 515, y: 230))
plasma.line(to: NSPoint(x: 1480, y: 230))
plasma.close()
orange.setFill()
plasma.fill()

// Vehicle body.
let vehicle = NSBezierPath()
vehicle.move(to: NSPoint(x: 1480, y: 440))
vehicle.line(to: NSPoint(x: 690, y: 440))
vehicle.curve(to: NSPoint(x: 430, y: 365), controlPoint1: NSPoint(x: 545, y: 440), controlPoint2: NSPoint(x: 430, y: 412))
vehicle.curve(to: NSPoint(x: 690, y: 300), controlPoint1: NSPoint(x: 430, y: 320), controlPoint2: NSPoint(x: 545, y: 300))
vehicle.line(to: NSPoint(x: 1480, y: 300))
vehicle.close()
gray.setFill()
vehicle.fill()

// The magnetic window: a clean gap over the system.
let windowGlow = NSBezierPath(ovalIn: NSRect(x: 650, y: 418, width: 300, height: 125))
NSColor.white.setFill()
windowGlow.fill()
let windowEdge = NSBezierPath()
windowEdge.move(to: NSPoint(x: 665, y: 443))
windowEdge.curve(to: NSPoint(x: 935, y: 465), controlPoint1: NSPoint(x: 750, y: 520), controlPoint2: NSPoint(x: 875, y: 520))
windowEdge.lineWidth = 5
windowEdge.lineCapStyle = .round
cyan.setStroke()
windowEdge.stroke()

// Magnetic system mounted on the vehicle.
roundedRect(NSRect(x: 718, y: 350, width: 175, height: 58), radius: 12, fill: navy)
roundedRect(NSRect(x: 738, y: 366, width: 52, height: 26), radius: 5, fill: color(0xEF4E4E))
roundedRect(NSRect(x: 821, y: 366, width: 52, height: 26), radius: 5, fill: cyan)
text("N", x: 755, y: 368, size: 14, weight: .bold, fill: .white, width: 20, alignment: .center)
text("S", x: 838, y: 368, size: 14, weight: .bold, fill: .white, width: 20, alignment: .center)

// Magnetic field arcs.
for (i, inset) in [CGFloat(0), 22, 44].enumerated() {
    let field = NSBezierPath()
    field.move(to: NSPoint(x: 735 + inset, y: 410))
    field.curve(to: NSPoint(x: 878 - inset, y: 410), controlPoint1: NSPoint(x: 720 + inset, y: 520 + CGFloat(i) * 12), controlPoint2: NSPoint(x: 900 - inset, y: 520 + CGFloat(i) * 12))
    field.lineWidth = 3
    field.setLineDash([9, 8], count: 2, phase: CGFloat(i) * 4)
    field.lineCapStyle = .round
    cyan.setStroke()
    field.stroke()
}

// Satellite and radio link through the window.
roundedRect(NSRect(x: 205, y: 535, width: 58, height: 38), radius: 6, fill: navy)
roundedRect(NSRect(x: 128, y: 541, width: 65, height: 26), radius: 3, fill: blue)
roundedRect(NSRect(x: 275, y: 541, width: 65, height: 26), radius: 3, fill: blue)
line(from: NSPoint(x: 234, y: 573), to: NSPoint(x: 234, y: 601), stroke: navy, width: 4)
let dish = NSBezierPath()
dish.move(to: NSPoint(x: 218, y: 604))
dish.curve(to: NSPoint(x: 252, y: 604), controlPoint1: NSPoint(x: 228, y: 622), controlPoint2: NSPoint(x: 243, y: 622))
dish.lineWidth = 4
navy.setStroke()
dish.stroke()
arrow(from: NSPoint(x: 310, y: 550), to: NSPoint(x: 700, y: 500), stroke: navy, width: 4)
for offset in [CGFloat(0), 22, 44] {
    let wave = NSBezierPath()
    wave.move(to: NSPoint(x: 360 + offset, y: 548 - offset * 0.10))
    wave.curve(to: NSPoint(x: 440 + offset, y: 538 - offset * 0.10), controlPoint1: NSPoint(x: 390 + offset, y: 570), controlPoint2: NSPoint(x: 420 + offset, y: 558))
    wave.lineWidth = 3
    cyan.setStroke()
    wave.stroke()
}

// Labels and leader lines.
roundedRect(NSRect(x: 1030, y: 470, width: 380, height: 58), radius: 12, fill: NSColor.white.withAlphaComponent(0.92))
text("Plasma sheath", x: 1054, y: 455, size: 22, weight: .semibold, fill: orange, width: 310)
line(from: NSPoint(x: 1030, y: 493), to: NSPoint(x: 975, y: 490), stroke: orange, width: 3)

roundedRect(NSRect(x: 1030, y: 360, width: 380, height: 58), radius: 12, fill: NSColor.white.withAlphaComponent(0.92))
text("Magnetic system", x: 1054, y: 345, size: 22, weight: .semibold, fill: navy, width: 310)
line(from: NSPoint(x: 1030, y: 385), to: NSPoint(x: 900, y: 380), stroke: navy, width: 3)

roundedRect(NSRect(x: 570, y: 570, width: 330, height: 58), radius: 12, fill: NSColor.white.withAlphaComponent(0.95))
text("Communication window", x: 592, y: 555, size: 21, weight: .semibold, fill: blue, width: 285)
line(from: NSPoint(x: 735, y: 570), to: NSPoint(x: 790, y: 535), stroke: blue, width: 3)

// Small caption inside vehicle.
text("HYPERSONIC VEHICLE", x: 1060, y: 315, size: 18, weight: .semibold, fill: darkGray, width: 330, alignment: .center)

// Bottom explanatory key.
text("The magnetic field redirects charged particles, creating a brief path for radio-frequency communication.", x: 110, y: 82, size: 21, weight: .regular, fill: darkGray, width: 1380, alignment: .center)

NSGraphicsContext.restoreGraphicsState()
try FileManager.default.createDirectory(atPath: "img", withIntermediateDirectories: true)
if let data = rep.representation(using: .png, properties: [:]) {
    try data.write(to: URL(fileURLWithPath: output))
    print("Wrote \(output)")
} else {
    fputs("Could not encode PNG\n", stderr)
    exit(1)
}
