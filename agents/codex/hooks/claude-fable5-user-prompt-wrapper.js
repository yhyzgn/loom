#!/usr/bin/env node
const fs = require('node:fs');
const path = require('node:path');
const { spawnSync } = require('node:child_process');

const OMX_HOOK = '/home/neo/.bun/install/global/node_modules/oh-my-codex/dist/scripts/codex-native-hook.js';
const NODE = process.execPath;

function readStdin() {
  return fs.readFileSync(0, 'utf8');
}

function safeJsonParse(text) {
  if (!String(text || '').trim()) return null;
  try { return JSON.parse(text); } catch { return null; }
}

function eventName(payload) {
  return String(payload?.hook_event_name || payload?.hookEventName || payload?.event_name || payload?.eventName || '').trim();
}

function buildFableContext() {
  if (process.env.CLAUDE_FABLE5_DEFAULT_HOOK === '0') return '';
  const home = process.env.HOME || '/home/neo';
  const skillDir = path.join(home, '.codex', 'skills', 'claude-fable5');
  const skillPath = path.join(skillDir, 'SKILL.md');
  const corePath = path.join(skillDir, 'references', 'fable5-core.md');
  if (!fs.existsSync(skillPath) || !fs.existsSync(corePath)) return '';
  return [
    '[Default persona skill]',
    'Use the user-level `$claude-fable5` skill as a default response style/safety adapter for this turn.',
    `Before applying it, load and follow ${skillPath} and ${corePath}.`,
    'This is a Codex-safe Fable5-inspired adapter only: preserve Codex/OpenAI identity, AGENTS.md/OMX precedence, tool schemas, and higher-priority safety rules.',
    'Do not load the full original source prompt unless the user explicitly asks to inspect, compare, audit, quote, or port source-level details.'
  ].join('\n');
}

function emit(value) {
  process.stdout.write(JSON.stringify(value) + '\n');
}

const stdin = readStdin();
const payload = safeJsonParse(stdin) || {};
const child = spawnSync(NODE, [OMX_HOOK], {
  input: stdin,
  encoding: 'utf8',
  env: process.env,
  maxBuffer: 10 * 1024 * 1024,
});

const childStdout = String(child.stdout || '').trim();
const childStderr = String(child.stderr || '');
const childJson = safeJsonParse(childStdout);

if (childStderr) process.stderr.write(childStderr);

const fableContext = eventName(payload) === 'UserPromptSubmit' ? buildFableContext() : '';

if (!fableContext) {
  if (childStdout) process.stdout.write(childStdout + (childStdout.endsWith('\n') ? '' : '\n'));
  process.exit(child.status ?? 0);
}

if (!childJson) {
  emit({
    hookSpecificOutput: {
      hookEventName: 'UserPromptSubmit',
      additionalContext: fableContext,
    },
  });
  process.exit(child.status ?? 0);
}

const output = childJson;
const hookSpecificOutput = output.hookSpecificOutput && typeof output.hookSpecificOutput === 'object'
  ? output.hookSpecificOutput
  : {};
const existingContext = typeof hookSpecificOutput.additionalContext === 'string'
  ? hookSpecificOutput.additionalContext.trim()
  : '';
output.hookSpecificOutput = {
  ...hookSpecificOutput,
  hookEventName: hookSpecificOutput.hookEventName || 'UserPromptSubmit',
  additionalContext: existingContext ? `${existingContext}\n\n${fableContext}` : fableContext,
};

emit(output);
process.exit(child.status ?? 0);
