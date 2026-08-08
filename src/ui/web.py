import json
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from src.storage.database import TraceDatabase
from src.storage.time_travel import TimeTravelEngine


HOST = "127.0.0.1"
PORT = 8000


HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>PyChronicle - Time Travel Debugger</title>

<style>

* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    min-height: 100%;
}

body {
    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    color: #f4f7ff;

    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(42, 95, 150, 0.22),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #07101b 0%,
            #0b1420 50%,
            #101927 100%
        );

    min-height: 100vh;
    overflow-x: hidden;
}


/* =========================================================
   FOG
   ========================================================= */

.fog {
    position: absolute;
    top: 0;
    left: -10%;
    width: 120%;
    height: 190px;

    pointer-events: none;

    background:
        radial-gradient(
            ellipse at 20% 55%,
            rgba(255,255,255,0.18),
            transparent 38%
        ),
        radial-gradient(
            ellipse at 50% 45%,
            rgba(255,255,255,0.14),
            transparent 40%
        ),
        radial-gradient(
            ellipse at 80% 60%,
            rgba(255,255,255,0.16),
            transparent 38%
        );

    filter: blur(24px);

    animation:
        fogMove 12s ease-in-out infinite alternate;

    z-index: 0;
}

@keyframes fogMove {

    from {
        transform: translateY(-10px) scaleX(1);
        opacity: 0.65;
    }

    to {
        transform: translateY(35px) scaleX(1.08);
        opacity: 0.9;
    }
}


/* =========================================================
   HEADER
   ========================================================= */

.header {
    position: relative;

    text-align: center;

    padding:
        26px
        20px
        30px;

    overflow: hidden;
}

.title {
    position: relative;

    margin: 0;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(42px, 6vw, 78px);

    letter-spacing: 1px;

    color: #f7fbff;

    text-shadow:
        0 0 8px rgba(180,220,255,0.8),
        0 0 22px rgba(74,160,255,0.8),
        0 0 45px rgba(73,103,255,0.55);

    animation:
        titleBlink 3.2s ease-in-out infinite;
}


/* blinking title cursor */

.title::after {
    content: "|";

    margin-left: 7px;

    color: #ffffff;

    animation:
        cursorBlink 1s steps(1) infinite;
}

@keyframes titleBlink {

    0%,
    100% {
        opacity: 1;

        text-shadow:
            0 0 8px rgba(180,220,255,0.8),
            0 0 22px rgba(74,160,255,0.8),
            0 0 45px rgba(73,103,255,0.55);
    }

    50% {
        opacity: 0.78;

        text-shadow:
            0 0 5px rgba(180,220,255,0.4),
            0 0 12px rgba(74,160,255,0.4);
    }
}

@keyframes cursorBlink {

    0%,
    45% {
        opacity: 1;
    }

    46%,
    100% {
        opacity: 0;
    }
}

.subtitle {
    position: relative;

    margin-top: 8px;

    color: #d8e1ef;

    font-size: 18px;

    letter-spacing: 0.5px;
}


/* =========================================================
   MAIN LAYOUT
   ========================================================= */

.container {
    position: relative;
    z-index: 2;

    width: min(1500px, 96%);

    margin: auto;

    display: grid;

    grid-template-columns:
        minmax(420px, 1fr)
        minmax(420px, 1fr);

    gap: 14px;
}


/* =========================================================
   PANELS
   ========================================================= */

.panel {
    background:
        linear-gradient(
            145deg,
            rgba(18, 29, 43, 0.94),
            rgba(8, 17, 28, 0.96)
        );

    border:
        1px solid rgba(120,170,220,0.28);

    border-radius: 10px;

    box-shadow:
        0 12px 35px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.03);

    overflow: hidden;
}

.panel-title {
    padding:
        17px
        22px;

    font-size: 18px;

    font-weight: 600;

    color: #36a7ff;

    letter-spacing: 0.3px;
}

.panel-body {
    padding: 14px 20px 20px;
}


/* =========================================================
   EDITOR
   ========================================================= */

.editor-panel {
    grid-row: span 3;
}

.editor {
    margin: 0;

    min-height: 500px;

    width: 100%;

    resize: vertical;

    border:
        1px solid rgba(120,170,220,0.22);

    border-radius: 8px;

    outline: none;

    background:
        #080d13;

    color: #dce7f7;

    padding: 20px;

    font-family:
        "Cascadia Code",
        "Consolas",
        monospace;

    font-size: 15px;

    line-height: 1.65;

    tab-size: 4;
}

.editor:focus {
    border-color: rgba(65,150,255,0.7);

    box-shadow:
        0 0 0 1px rgba(65,150,255,0.2);
}

.editor-footer {
    display: flex;

    align-items: center;

    justify-content: space-between;

    margin-top: 12px;

    color: #8192a8;

    font-size: 13px;
}


/* =========================================================
   BUTTON
   ========================================================= */

button {
    border: 0;

    border-radius: 7px;

    padding:
        11px
        22px;

    color: white;

    font-weight: 600;

    cursor: pointer;

    background:
        linear-gradient(
            135deg,
            #4d24d8,
            #7137ee
        );

    box-shadow:
        0 5px 18px rgba(104,52,238,0.28);

    transition:
        transform 0.15s,
        box-shadow 0.15s;
}

button:hover {
    transform: translateY(-1px);

    box-shadow:
        0 8px 22px rgba(104,52,238,0.45);
}

button:active {
    transform: translateY(0);
}


/* =========================================================
   CURRENT EVENT
   ========================================================= */

.event-box {
    border:
        1px solid rgba(120,170,220,0.2);

    border-radius: 8px;

    padding: 17px;

    background:
        rgba(10,18,29,0.72);
}

.event-grid {
    display: grid;

    grid-template-columns:
        130px
        1fr;

    row-gap: 10px;

    font-size: 14px;
}

.event-label {
    font-weight: 600;

    color: #f0f4fb;
}

.event-value {
    color: #d6e0ee;

    word-break: break-word;
}

.event-value.highlight {
    color: #45aaff;
}

.event-value.function {
    color: #c86cff;
}


/* =========================================================
   PROGRAM STATE
   ========================================================= */

.state-box {
    min-height: 100px;

    border:
        1px solid rgba(120,170,220,0.2);

    border-radius: 8px;

    padding: 16px;

    background:
        rgba(7,14,22,0.82);

    color: #50e29c;

    font-family:
        "Cascadia Code",
        Consolas,
        monospace;

    white-space: pre-wrap;

    overflow-x: auto;
}


/* =========================================================
   NAVIGATION
   ========================================================= */

.nav-buttons {
    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 9px;

    margin-bottom: 18px;
}

.nav-buttons button {
    background:
        linear-gradient(
            145deg,
            #242d38,
            #171f29
        );

    border:
        1px solid rgba(150,180,210,0.18);

    box-shadow: none;
}

.nav-buttons button:hover {
    border-color: rgba(75,165,255,0.55);
}

.nav-buttons .next {
    background:
        linear-gradient(
            135deg,
            #1266db,
            #267ff2
        );
}

.jump-row {
    display: flex;

    gap: 10px;
}

.jump-input {
    flex: 1;

    min-width: 0;

    padding: 12px 14px;

    border:
        1px solid rgba(120,170,220,0.25);

    border-radius: 7px;

    outline: none;

    background: #09121d;

    color: white;

    font-size: 14px;
}

.jump-input:focus {
    border-color: #318df5;
}

.position {
    margin-top: 14px;

    padding: 10px;

    border:
        1px solid rgba(120,170,220,0.12);

    border-radius: 6px;

    color: #48aaff;

    font-size: 13px;

    background: rgba(10,18,28,0.7);
}


/* =========================================================
   OUTPUT
   ========================================================= */

.output-panel {
    margin-top: 14px;
}

.output {
    min-height: 85px;

    border:
        1px solid rgba(120,170,220,0.2);

    border-radius: 8px;

    background: #080e15;

    padding: 16px;

    color: #64e6a6;

    font-family:
        "Cascadia Code",
        Consolas,
        monospace;

    white-space: pre-wrap;
}


/* =========================================================
   STATUS
   ========================================================= */

.status {
    min-height: 20px;

    margin-top: 10px;

    color: #f1a8a8;

    font-size: 13px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    position: relative;
    z-index: 2;

    text-align: center;

    padding:
        24px
        10px;

    color: #8290a2;

    font-size: 13px;
}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 900px) {

    .container {
        grid-template-columns: 1fr;
    }

    .editor-panel {
        grid-row: auto;
    }

    .editor {
        min-height: 350px;
    }
}

</style>
</head>


<body>

<div class="fog"></div>


<header class="header">

    <h1 class="title">PyChronicle</h1>

    <div class="subtitle">
        Python Time Travel Debugger
    </div>

</header>


<main class="container">


    <!-- =====================================================
         LEFT: PYTHON PROGRAM
         ===================================================== -->

    <section class="panel editor-panel">

        <div class="panel-title">
            &lt;/&gt;&nbsp;&nbsp; Write Your Python Program
        </div>

        <div class="panel-body">

<textarea
id="program"
class="editor"
spellcheck="false">def add(a, b):
    total = a + b
    return total

x = 10
y = 20

result = add(x, y)
print(result)</textarea>


            <div class="editor-footer">

                <span>Python 3.x</span>

                <button onclick="runProgram()">
                    &#9654;&nbsp; Run Program
                </button>

            </div>

        </div>

    </section>


    <!-- =====================================================
         RIGHT: CURRENT EVENT
         ===================================================== -->

    <section class="panel">

        <div class="panel-title">
            &#12309;&nbsp;&nbsp; Current Event
        </div>

        <div class="panel-body">

            <div class="event-box">

                <div class="event-grid">

                    <div class="event-label">Event ID</div>
                    <div class="event-value"
                         id="event-id">-</div>

                    <div class="event-label">Event</div>
                    <div class="event-value highlight"
                         id="event-type">-</div>

                    <div class="event-label">Function</div>
                    <div class="event-value function"
                         id="function">-</div>

                    <div class="event-label">Line</div>
                    <div class="event-value"
                         id="line">-</div>

                    <div class="event-label">Variable</div>
                    <div class="event-value"
                         id="variable">-</div>

                    <div class="event-label">Value</div>
                    <div class="event-value"
                         id="value">-</div>

                    <div class="event-label">Timestamp</div>
                    <div class="event-value"
                         id="timestamp">-</div>

                </div>

            </div>

        </div>

    </section>


    <!-- =====================================================
         RIGHT: PROGRAM STATE
         ===================================================== -->

    <section class="panel">

        <div class="panel-title">
            &#9673;&nbsp;&nbsp; Program State
        </div>

        <div class="panel-body">

            <div
                id="state"
                class="state-box">{}</div>

        </div>

    </section>


    <!-- =====================================================
         RIGHT: NAVIGATION
         ===================================================== -->

    <section class="panel">

        <div class="panel-title">
            &#10023;&nbsp;&nbsp; Navigation
        </div>

        <div class="panel-body">

            <div class="nav-buttons">

                <button onclick="firstEvent()">
                    &#9664;&#9664; First
                </button>

                <button onclick="previousEvent()">
                    &#9664; Previous
                </button>

                <button
                    class="next"
                    onclick="nextEvent()">
                    Next &#9654;
                </button>

                <button onclick="lastEvent()">
                    Last &#9654;&#9654;
                </button>

            </div>


            <div
                style="
                    margin-bottom: 8px;
                    color: #f1f4fa;
                    font-weight: 600;
                ">
                Jump to Event ID
            </div>


            <div class="jump-row">

                <input
                    id="event-input"
                    class="jump-input"
                    type="number"
                    placeholder="Enter Event ID">

                <button onclick="jumpEvent()">
                    &#9673;&nbsp; Jump
                </button>

            </div>


            <div
                id="status"
                class="status">
            </div>


            <div
                id="position"
                class="position">
                Total Events: 0 | Current Position: 0 / 0
            </div>

        </div>

    </section>


    <!-- =====================================================
         LEFT: OUTPUT
         ===================================================== -->

    <section class="panel output-panel">

        <div class="panel-title">
            Program Output
        </div>

        <div class="panel-body">

            <div
                id="output"
                class="output"></div>

        </div>

    </section>


</main>


<footer class="footer">

    &copy; 2026 PyChronicle &ndash; Python Time Travel Debugger

</footer>


<script>


/* =========================================================
   DISPLAY EVENT
   ========================================================= */

function displayEvent(event) {

    if (!event) {
        return;
    }

    document.getElementById("event-id").textContent =
        event.id ?? "-";

    document.getElementById("event-type").textContent =
        event.event ?? "-";

    document.getElementById("function").textContent =
        event.function || "<module>";

    document.getElementById("line").textContent =
        event.line ?? "-";

    document.getElementById("variable").textContent =
        event.variable ?? "-";

    document.getElementById("value").textContent =
        event.value ?? "-";

    document.getElementById("timestamp").textContent =
        event.timestamp ?? "-";
}


/* =========================================================
   DISPLAY STATE
   ========================================================= */

function displayState(state) {

    document.getElementById("state").textContent =
        JSON.stringify(state || {}, null, 4);
}


/* =========================================================
   POSITION
   ========================================================= */

function displayPosition(position) {

    if (!position) {
        return;
    }

    document.getElementById("position").textContent =
        "Total Events: " +
        position.total +
        " | Current Position: " +
        position.current +
        " / " +
        position.total;
}


/* =========================================================
   STATUS
   ========================================================= */

function showStatus(message) {

    document.getElementById("status").textContent =
        message || "";
}


/* =========================================================
   CURRENT
   ========================================================= */

async function loadCurrent() {

    const response =
        await fetch("/api/current");

    const data =
        await response.json();

    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

    } else {

        showStatus(
            "No execution events available."
        );
    }
}


/* =========================================================
   NEXT
   ========================================================= */

async function nextEvent() {

    const response =
        await fetch("/api/next");

    const data =
        await response.json();

    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

        showStatus("");

    }
}


/* =========================================================
   PREVIOUS
   ========================================================= */

async function previousEvent() {

    const response =
        await fetch("/api/previous");

    const data =
        await response.json();

    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

        showStatus("");

    }
}


/* =========================================================
   FIRST
   ========================================================= */

async function firstEvent() {

    const response =
        await fetch("/api/first");

    const data =
        await response.json();

    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

        showStatus("");

    }
}


/* =========================================================
   LAST
   ========================================================= */

async function lastEvent() {

    const response =
        await fetch("/api/last");

    const data =
        await response.json();

    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

        showStatus("");

    }
}


/* =========================================================
   JUMP
   ========================================================= */

async function jumpEvent() {

    const eventId =
        document.getElementById(
            "event-input"
        ).value;

    if (!eventId) {

        showStatus(
            "Enter an event ID."
        );

        return;
    }


    const response =
        await fetch(
            "/api/jump?id=" + eventId
        );

    const data =
        await response.json();


    if (data.event) {

        displayEvent(data.event);

        displayState(data.state);

        displayPosition(data.position);

        showStatus("");

    } else {

        showStatus(
            "Event " + eventId + " not found."
        );
    }
}


/* =========================================================
   RUN PROGRAM
   ========================================================= */

async function runProgram() {

    const program =
        document.getElementById(
            "program"
        ).value;


    if (!program.trim()) {

        showStatus(
            "Write a Python program first."
        );

        return;
    }


    showStatus(
        "Running program..."
    );


    const response =
        await fetch(
            "/api/run",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    program: program
                })
            }
        );


    const data =
        await response.json();


    if (data.success) {

        document.getElementById(
            "output"
        ).textContent =
            data.output || "";

        showStatus("");

        await loadCurrent();

    } else {

        document.getElementById(
            "output"
        ).textContent =
            data.output || data.error || "";

        showStatus(
            "Program execution failed."
        );
    }
}


/* =========================================================
   LOAD PAGE
   ========================================================= */

loadCurrent();

</script>

</body>
</html>
"""


class WebState:

    def __init__(self):
        self.database = TraceDatabase()
        self.events = self.database.fetch_event_objects()
        self.engine = TimeTravelEngine(self.events)

    def reload(self):
        self.events = self.database.fetch_event_objects()
        self.engine = TimeTravelEngine(self.events)

    def position(self):
        total = len(self.engine.events)

        if total == 0:
            return {
                "current": 0,
                "total": 0
            }

        return {
            "current": self.engine.current_index + 1,
            "total": total
        }

    def close(self):
        self.database.close()


web_state = WebState()


class RequestHandler(BaseHTTPRequestHandler):

    @staticmethod
    def extract_program_output(output):
        """
        Extract only the user's program output from main.py output.

        PyChronicle's internal tracer/database/timeline diagnostics
        are kept out of the browser Output panel.
        """

        lines = output.splitlines()

        clean_lines = []

        for line in lines:

            # Stop before PyChronicle's internal diagnostics.
            if line.strip() == "RUNTIME EVENTS":
                break

            # Remove tracer display lines.
            if line.lstrip().startswith(
                ("[CALL", "[LINE", "[RETURN")
            ):
                continue

            # Remove separator lines.
            if line.strip() and set(line.strip()) == {"="}:
                continue

            clean_lines.append(line)

        return "\n".join(clean_lines).strip()

    def send_json(self, data):
        response = json.dumps(data, default=str).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def send_html(self):
        response = HTML.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        query = parse_qs(parsed.query)

        if path == "/":
            self.send_html()
            return

        if path == "/api/current":
            event = web_state.engine.current()

            self.send_json({
                "event": event,
                "state": web_state.engine.state(),
                "position": web_state.position()
            })

            return

        if path == "/api/next":
            event = web_state.engine.next()

            self.send_json({
                "event": event,
                "state": web_state.engine.state(),
                "position": web_state.position()
            })

            return

        if path == "/api/previous":
            event = web_state.engine.previous()

            self.send_json({
                "event": event,
                "state": web_state.engine.state(),
                "position": web_state.position()
            })

            return

        if path == "/api/first":
            if web_state.engine.events:
                web_state.engine.current_index = 0

            event = web_state.engine.current()

            self.send_json({
                "event": event,
                "state": web_state.engine.state(),
                "position": web_state.position()
            })

            return

        if path == "/api/last":
            if web_state.engine.events:
                web_state.engine.current_index = (
                    len(web_state.engine.events) - 1
                )

            event = web_state.engine.current()

            self.send_json({
                "event": event,
                "state": web_state.engine.state(),
                "position": web_state.position()
            })

            return

        if path == "/api/jump":
            try:
                event_id = int(query.get("id", [0])[0])
            except ValueError:
                self.send_json({
                    "event": None,
                    "state": {},
                    "position": web_state.position()
                })

                return

            event = web_state.engine.jump(event_id)

            self.send_json({
                "event": event,
                "state": (
                    web_state.engine.state()
                    if event is not None
                    else {}
                ),
                "position": web_state.position()
            })

            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path != "/api/run":
            self.send_response(404)
            self.end_headers()
            return

        try:
            content_length = int(
                self.headers.get("Content-Length", 0)
            )

            body = self.rfile.read(content_length)
            data = json.loads(body.decode("utf-8"))
            program = data.get("program", "")

            if not program.strip():
                self.send_json({
                    "success": False,
                    "error": "Program is empty."
                })

                return

            program_path = "examples/runtime_demo.py"

            with open(program_path, "w", encoding="utf-8") as file:
                file.write(program)

            result = subprocess.run(
                [sys.executable, "main.py"],
                capture_output=True,
                text=True
            )

            output = self.extract_program_output(
                result.stdout
            )

            if result.stderr:
                if output:
                    output += "\n"

                output += result.stderr.strip()

            web_state.reload()

            self.send_json({
                "success": result.returncode == 0,
                "output": output,
                "error": None
            })

        except Exception as exc:
            self.send_json({
                "success": False,
                "output": "",
                "error": str(exc)
            })


def start_server():
    server = HTTPServer((HOST, PORT), RequestHandler)

    print()
    print("=" * 60)
    print("PYCHRONICLE WEB UI")
    print("=" * 60)
    print(f"Open http://{HOST}:{PORT}")
    print("Press Ctrl+C to stop.")
    print("=" * 60)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        web_state.close()
        server.server_close()


if __name__ == "__main__":
    start_server()