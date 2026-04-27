import sys


def format_val(v):
    if isinstance(v, bool):
        return 'true' if v else 'false'
    return str(v)


def run(instructions):
    stack = []
    variables = {}

    # Preindexuj navesti pro skoky
    labels = {}
    for i, line in enumerate(instructions):
        parts = line.split()
        if parts and parts[0] == 'label':
            labels[int(parts[1])] = i

    pc = 0
    while pc < len(instructions):
        line = instructions[pc]
        parts = line.split()

        if not parts:
            pc += 1
            continue

        instr = parts[0]

        if instr == 'push':
            typ = parts[1]
            if typ == 'I':
                stack.append(int(parts[2]))
            elif typ == 'F':
                stack.append(float(parts[2]))
            elif typ == 'B':
                stack.append(parts[2] == 'true')
            elif typ == 'S':
                # Zrekonstruuj retezec vcetne mezer, odstran uvozovky
                val = line[len('push S '):]
                stack.append(val[1:-1])

        elif instr == 'pop':
            stack.pop()

        elif instr == 'load':
            stack.append(variables[parts[1]])

        elif instr == 'save':
            variables[parts[1]] = stack.pop()

        elif instr == 'add':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif instr == 'sub':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif instr == 'mul':
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)

        elif instr == 'div':
            b = stack.pop()
            a = stack.pop()
            if parts[1] == 'I':
                stack.append(int(a / b))
            else:
                stack.append(a / b)

        elif instr == 'mod':
            b = stack.pop()
            a = stack.pop()
            stack.append(a % b)

        elif instr == 'uminus':
            stack.append(-stack.pop())

        elif instr == 'concat':
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)

        elif instr == 'and':
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)

        elif instr == 'or':
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)

        elif instr == 'not':
            stack.append(not stack.pop())

        elif instr == 'lt':
            b = stack.pop()
            a = stack.pop()
            stack.append(a < b)

        elif instr == 'gt':
            b = stack.pop()
            a = stack.pop()
            stack.append(a > b)

        elif instr == 'eq':
            b = stack.pop()
            a = stack.pop()
            stack.append(a == b)

        elif instr == 'charat':
            idx = stack.pop()
            s = stack.pop()
            stack.append(s[idx])

        elif instr == 'len':
            stack.append(len(stack.pop()))

        elif instr == 'fopen':
            filename = stack.pop()
            stack.append(open(filename, 'w'))

        elif instr == 'fwrite':
            n = int(parts[1])
            items = stack[-n:]
            del stack[-n:]
            f = items[0]
            for v in items[1:]:
                f.write(format_val(v))
            f.write('\n')

        elif instr == 'fappend':
            n = int(parts[1])
            items = stack[-n:]
            del stack[-n:]
            f = items[0]
            for v in items[1:]:
                f.write(format_val(v))
            f.write('\n')

        elif instr == 'itof':
            stack.append(float(stack.pop()))

        elif instr == 'label':
            pass  # navesti je jen znacka, nic nedelame

        elif instr == 'jmp':
            pc = labels[int(parts[1])]
            continue

        elif instr == 'fjmp':
            val = stack.pop()
            if not val:
                pc = labels[int(parts[1])]
                continue

        elif instr == 'print':
            n = int(parts[1])
            vals = stack[-n:]
            del stack[-n:]
            for v in vals:
                print(format_val(v), end='')
            print()

        elif instr == 'read':
            typ = parts[1]
            line_in = input()
            try:
                if typ == 'I':
                    stack.append(int(line_in))
                elif typ == 'F':
                    stack.append(float(line_in))
                elif typ == 'B':
                    v = line_in.strip()
                    if v not in ('true', 'false'):
                        raise ValueError
                    stack.append(v == 'true')
                elif typ == 'S':
                    stack.append(line_in)
            except ValueError:
                print(f"Chyba: spatny vstup pro typ {typ}")
                sys.exit(1)

        pc += 1

    for v in variables.values():
        if hasattr(v, 'close'):
            v.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Pouziti: python interpreter.py <soubor_s_instrukcemi>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        instructions = [line.rstrip('\n') for line in f.readlines()]

    run(instructions)
