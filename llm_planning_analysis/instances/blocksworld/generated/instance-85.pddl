(define (problem BW-generalization-4)
(:domain blocksworld-4ops)(:objects d e b k a g h f j i)
(:init 
(handempty)
(ontable d)
(ontable e)
(ontable b)
(ontable k)
(ontable a)
(ontable g)
(ontable h)
(ontable f)
(ontable j)
(ontable i)
(clear d)
(clear e)
(clear b)
(clear k)
(clear a)
(clear g)
(clear h)
(clear f)
(clear j)
(clear i)
)
(:goal
(and
(on d e)
(on e b)
(on b k)
(on k a)
(on a g)
(on g h)
(on h f)
(on f j)
(on j i)
)))