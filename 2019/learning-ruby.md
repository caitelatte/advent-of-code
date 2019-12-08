# learning ruby

https://ruby.github.io/TryRuby/

- some methods can do `!` at the end to do the action in place, eg:

  ```ruby
  puts ticket.sort
  puts ticket
  # variable not affected

  puts ticket.sort!
  puts ticket
  # variable affected in place
  ```

- **symbol** - put a colon in front of a word. cheaper than a string in memory
- **blocks** - code after a method, eg:

  ```ruby
  5.times { print "0delay! " }
  ```

  - pass values to a block with pipes, eg:

    ```ruby
    5.times { |time}
      puts time
    }
    ```

  - iterate with `.each`
- *if/else/end*
- **classes**
  - attributes examples (inside the class, at symbols for variables, outside use accessors): 

    ```ruby
    class Blurb
      attr_accessor :content, :time, :mood

      def initialise(mood, content="")
        @time = Time.now
        @content = content[0..39]
        @mood = mood
      end
    end
    ```
- append to end of array with `<<`
- nice string evaluation with `"#{@variable}"` but not with single quote strings

  ```ruby
  "Blurbify: #{@title} has #{@blurbs.count} Blurbs"
  ```