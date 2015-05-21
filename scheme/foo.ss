;; chp 3.1
;; 累加器

(define (make-acc n)
  (define (acc x)
    (+ x n))
  acc)

;; chp 3.2

