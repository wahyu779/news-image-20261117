// The Daily World — Tuesday 17 November 2026.
// Entry program: the front page is a finished image (entry.png), rendered
// beforehand from page.html with render.py. This program only delivers
// that image to the output directory, byte for byte, so every run of the
// entry produces identical output.

const outDir = Deno.env.get("MAKEFUN_OUTPUT_DIR");
if (!outDir) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}

const source = new URL("./entry.png", import.meta.url);
await Deno.copyFile(source, `${outDir}/output.png`);
