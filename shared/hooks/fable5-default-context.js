#!/usr/bin/env node
const fs = require('node:fs');
const path = require('node:path');

function parseArgs(argv) {
  const out = { platform: 'agent', event: '' };
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] === '--platform') out.platform = argv[++i] || out.platform;
    else if (argv[i] === '--event') out.event = argv[++i] || out.event;
  }
  return out;
}
function readStdin() { try { return fs.readFileSync(0, 'utf8'); } catch { return ''; } }
function parsePayload(raw) { try { return raw.trim() ? JSON.parse(raw) : {}; } catch { return {}; } }
function eventName(payload, fallback) {
  return String(payload.hook_event_name || payload.hookEventName || payload.event_name || payload.eventName || fallback || 'SessionStart').trim();
}

const args = parseArgs(process.argv);
if (process.env.FABLE5_DEFAULT_HOOK === '0') process.exit(0);
const base = '/home/neo/.agent-personas/claude-fable5';
const core = path.join(base, 'core.md');
if (!fs.existsSync(core)) process.exit(0);
const payload = parsePayload(readStdin());
const hookEventName = eventName(payload, args.event);
const platform = args.platform;
const additionalContext = [
  `[Default Fable5 persona adapter: ${platform}]`,
  `Apply the local Fable5-inspired profile from ${core}.`,
  'Preserve this host agent identity, tool schema, safety policy, and all higher-priority workspace/project instructions.',
  'Do not load the full original prompt unless the user explicitly asks for source-level comparison, audit, quotation, or migration details.',
  'Summary: warm/direct style, evidence-driven answers, one-question max when clarification is needed, production-grade coding, cautious safety refusals.'
].join('\n');
process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName, additionalContext } }) + '\n');
