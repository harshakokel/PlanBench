

(define (problem BW-rand-4)
(:domain blocksworld-4ops)
(:objects a b c d )
(:init
(handempty)
(on a b)
(ontable b)
(on c a)
(on d c)
(clear d)
)
(:goal
	(and
		(on a b)
		(on d c)
		(on b a)
	)
)
)