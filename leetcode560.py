from manim import *

class LeetCode560(Scene):
    def construct(self):

        nums = [1, 2, 3, -2, 2]
        k = 3

        prefix = {0: 1}
        current_sum = 0
        answer = 0

        ############################################################
        # TITLE
        ############################################################

        title = Text(
            "LeetCode 560 : Subarray Sum Equals K",
            font_size=42
        ).to_edge(UP)

        self.play(Write(title))
        self.wait()

        ############################################################
        # ARRAY
        ############################################################

        cells = VGroup()

        for n in nums:
            sq = Square(0.8)
            txt = Text(str(n), font_size=30)
            txt.move_to(sq.get_center())
            cells.add(VGroup(sq, txt))

        cells.arrange(RIGHT, buff=0.15)
        cells.shift(UP * 1.5)

        indices = VGroup()

        for i in range(len(nums)):
            t = Text(str(i), font_size=20)
            t.next_to(cells[i], DOWN)
            indices.add(t)

        self.play(Create(cells))
        self.play(FadeIn(indices))

        ############################################################
        # POINTER
        ############################################################

        pointer = Arrow(
            start=UP,
            end=DOWN,
            buff=0.1
        ).scale(0.6)

        pointer.next_to(cells[0], UP)

        self.play(GrowArrow(pointer))

        ############################################################
        # VARIABLES
        ############################################################

        current_text = Text(
            "Current Prefix = 0",
            font_size=30
        ).to_corner(UL)

        answer_text = Text(
            "Answer = 0",
            font_size=30
        ).next_to(current_text, DOWN)

        formula = Text(
            "Need = CurrentPrefix - k",
            font_size=28,
            color=YELLOW
        )

        formula.to_corner(UR)

        formula.to_corner(UR)

        self.play(
            Write(current_text),
            Write(answer_text),
            Write(formula)
        )

        ############################################################
        # HASHMAP
        ############################################################

        hashmap_title = Text(
            "Prefix HashMap",
            font_size=28
        )

        hashmap_title.to_edge(RIGHT).shift(DOWN * 1)

        hashmap_box = SurroundingRectangle(
            hashmap_title,
            buff=0.3
        )

        hashmap_entries = VGroup()

        self.play(
            Write(hashmap_title),
            Create(hashmap_box)
        )

        ############################################################
        # PREFIX HISTORY
        ############################################################

        prefix_history = [0]

        ############################################################
        # LOOP
        ############################################################

        for i, value in enumerate(nums):

            if i > 0:
                self.play(pointer.animate.next_to(cells[i], UP))

            #######################################################
            # Highlight current cell
            #######################################################

            self.play(cells[i][0].animate.set_fill(YELLOW, opacity=0.5))

            current_sum += value
            need = current_sum - k

            #######################################################
            # Update prefix sum text
            #######################################################

            new_current = Text(
                f"Current Prefix = {current_sum}",
                font_size=30
            ).move_to(current_text)

            self.play(Transform(current_text, new_current))

            #######################################################
            # Formula
            #######################################################

            equation = Text(
                f"{current_sum} - {k} = {need}",
                font_size=28,
                color=WHITE
            )

            equation.next_to(formula, DOWN)

            self.play(Write(equation))

            #######################################################
            # Lookup hashmap
            #######################################################

            lookup = Text(
                f"Lookup {need}",
                font_size=26,
                color=BLUE
            )

            lookup.next_to(equation, DOWN)

            self.play(Write(lookup))

            found = prefix.get(need, 0)

            result_text = Text(
                f"Found = {found}",
                font_size=28,
                color=GREEN if found else RED
            )

            result_text.next_to(lookup, DOWN)

            self.play(Write(result_text))

            #######################################################
            # If found, explain
            #######################################################

            if found:

                answer += found

                new_answer = Text(
                    f"Answer = {answer}",
                    font_size=30
                ).move_to(answer_text)

                self.play(Transform(answer_text, new_answer))

                ###################################################
                # Highlight subarray
                ###################################################

                target = current_sum - k

                running = 0
                start = -1

                for j in range(len(prefix_history)):
                    if prefix_history[j] == target:
                        start = j
                        break

                if start != -1:

                    highlight = VGroup()

                    for x in range(start, i + 1):
                        highlight.add(cells[x])

                    self.play(
                        highlight.animate.set_fill(
                            GREEN,
                            opacity=0.6
                        )
                    )

                    self.wait(0.8)

                    self.play(
                        highlight.animate.set_fill(
                            BLACK,
                            opacity=0
                        )
                    )

            #######################################################
            # Update hashmap
            #######################################################

            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            prefix_history.append(current_sum)

            hashmap_entries_new = VGroup()

            for key in sorted(prefix.keys()):

                line = Text(
                    f"{key} : {prefix[key]}",
                    font_size=22
                )

                hashmap_entries_new.add(line)

            hashmap_entries_new.arrange(
                DOWN,
                aligned_edge=LEFT
            )

            hashmap_entries_new.next_to(
                hashmap_box,
                DOWN
            )

            self.play(
                Transform(
                    hashmap_entries,
                    hashmap_entries_new
                )
            )

            #######################################################
            # Cleanup
            #######################################################

            self.play(
                FadeOut(equation),
                FadeOut(lookup),
                FadeOut(result_text)
            )

            self.play(
                cells[i][0].animate.set_fill(
                    BLACK,
                    opacity=0
                )
            )

            self.wait(0.5)

        ############################################################
        # END
        ############################################################

        summary = Text(
            f"Total Subarrays = {answer}",
            font_size=40,
            color=YELLOW
        )

        summary.to_edge(DOWN)

        self.play(Write(summary))

        self.wait(3)